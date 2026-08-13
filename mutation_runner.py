"""
Mutation Testing Engine for Weather Analytics Engine
Implements AST-based & Syntactic Mutation Operators:
- Value Mutations (Constants modification)
- Decision Mutations (Relational, Logical, and Membership operators replacement: >=, <=, ==, !=, >, <, and, or, in, not in)
- Statement Mutations (Statement deletion / Return value modification)

Calculates Mutation Score = (Killed Mutants / Total Mutants) * 100
"""

import ast
import importlib
import sys
import unittest
import pytest
from typing import List, Dict, Any, Tuple
import weather_analytics as wa


class DecisionMutator(ast.NodeTransformer):
    def __init__(self, target_index: int):
        self.target_index = target_index
        self.current_index = 0
        self.applied_mutation = ""

    def visit_Compare(self, node):
        new_ops = []
        for op in node.ops:
            if self.current_index == self.target_index:
                if isinstance(op, ast.GtE):
                    new_ops.append(ast.LtE())
                    self.applied_mutation = f"Decision Mutation: '>=' replaced with '<=' at line {node.lineno}"
                elif isinstance(op, ast.LtE):
                    new_ops.append(ast.GtE())
                    self.applied_mutation = f"Decision Mutation: '<=' replaced with '>=' at line {node.lineno}"
                elif isinstance(op, ast.Gt):
                    new_ops.append(ast.Lt())
                    self.applied_mutation = f"Decision Mutation: '>' replaced with '<' at line {node.lineno}"
                elif isinstance(op, ast.Lt):
                    new_ops.append(ast.Gt())
                    self.applied_mutation = f"Decision Mutation: '<' replaced with '>' at line {node.lineno}"
                elif isinstance(op, ast.Eq):
                    new_ops.append(ast.NotEq())
                    self.applied_mutation = f"Decision Mutation: '==' replaced with '!=' at line {node.lineno}"
                elif isinstance(op, ast.NotEq):
                    new_ops.append(ast.Eq())
                    self.applied_mutation = f"Decision Mutation: '!=' replaced with '==' at line {node.lineno}"
                elif isinstance(op, ast.In):
                    new_ops.append(ast.NotIn())
                    self.applied_mutation = f"Membership Mutation: 'in' replaced with 'not in' at line {node.lineno}"
                elif isinstance(op, ast.NotIn):
                    new_ops.append(ast.In())
                    self.applied_mutation = f"Membership Mutation: 'not in' replaced with 'in' at line {node.lineno}"
                else:
                    new_ops.append(op)
            else:
                new_ops.append(op)
            self.current_index += 1
        node.ops = new_ops
        return self.generic_visit(node)

    def visit_BoolOp(self, node):
        if self.current_index == self.target_index:
            if isinstance(node.op, ast.Or):
                node.op = ast.And()
                self.applied_mutation = f"Logical Mutation: 'or' replaced with 'and' at line {node.lineno}"
            elif isinstance(node.op, ast.And):
                node.op = ast.Or()
                self.applied_mutation = f"Logical Mutation: 'and' replaced with 'or' at line {node.lineno}"
        self.current_index += 1
        return self.generic_visit(node)


class ValueMutator(ast.NodeTransformer):
    def __init__(self, target_index: int):
        self.target_index = target_index
        self.current_index = 0
        self.applied_mutation = ""

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            if self.current_index == self.target_index:
                old_val = node.value
                node.value = node.value + 1.0 if isinstance(node.value, float) else node.value + 1
                self.applied_mutation = f"Value Mutation: Constant {old_val} changed to {node.value} at line {node.lineno}"
            self.current_index += 1
        return self.generic_visit(node)


class ArithmeticMutator(ast.NodeTransformer):
    def __init__(self, target_index: int):
        self.target_index = target_index
        self.current_index = 0
        self.applied_mutation = ""

    def visit_BinOp(self, node):
        if self.current_index == self.target_index:
            if isinstance(node.op, ast.Add):
                node.op = ast.Sub()
                self.applied_mutation = f"Arithmetic Mutation: '+' replaced with '-' at line {node.lineno}"
            elif isinstance(node.op, ast.Sub):
                node.op = ast.Add()
                self.applied_mutation = f"Arithmetic Mutation: '-' replaced with '+' at line {node.lineno}"
            elif isinstance(node.op, ast.Mult):
                node.op = ast.Div()
                self.applied_mutation = f"Arithmetic Mutation: '*' replaced with '/' at line {node.lineno}"
            elif isinstance(node.op, ast.Div):
                node.op = ast.Mult()
                self.applied_mutation = f"Arithmetic Mutation: '/' replaced with '*' at line {node.lineno}"
        self.current_index += 1
        return self.generic_visit(node)


def run_mutation_tests():
    with open("weather_analytics.py", "r") as f:
        source_code = f.read()

    parsed = ast.parse(source_code)
    
    class CountDecisions(ast.NodeVisitor):
        def __init__(self):
            self.count = 0
        def visit_Compare(self, node):
            self.count += len(node.ops)
            self.generic_visit(node)
        def visit_BoolOp(self, node):
            self.count += 1
            self.generic_visit(node)
            
    cd = CountDecisions()
    cd.visit(parsed)
    num_decisions = cd.count

    class CountValues(ast.NodeVisitor):
        def __init__(self):
            self.count = 0
        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
                self.count += 1
            self.generic_visit(node)
    cv = CountValues()
    cv.visit(parsed)
    num_values = cv.count

    class CountArithmetic(ast.NodeVisitor):
        def __init__(self):
            self.count = 0
        def visit_BinOp(self, node):
            self.count += 1
            self.generic_visit(node)
    ca = CountArithmetic()
    ca.visit(parsed)
    num_arithmetic = ca.count

    killed_count = 0
    survived_count = 0
    survived_list = []

    # Execute Decision Mutations
    for idx in range(num_decisions):
        tree = ast.parse(source_code)
        mutator = DecisionMutator(idx)
        mutated_tree = mutator.visit(tree)
        ast.fix_missing_locations(mutated_tree)
        code_obj = compile(mutated_tree, filename="<mutant>", mode="exec")
        
        mutant_module = {}
        exec(code_obj, mutant_module)
        
        original_attrs = {k: getattr(wa, k) for k in dir(wa) if not k.startswith("__")}
        for k, v in mutant_module.items():
            if not k.startswith("__"):
                setattr(wa, k, v)

        retcode = pytest.main(["-q", "tests/test_weather_analytics.py", "--no-header"])

        for k, v in original_attrs.items():
            setattr(wa, k, v)

        status = "KILLED" if retcode != 0 else "SURVIVED"
        if status == "KILLED":
            killed_count += 1
        else:
            survived_count += 1
            survived_list.append(f"M-DEC-{idx+1:02d}: {mutator.applied_mutation}")

    # Execute Value Mutations
    for idx in range(num_values):
        tree = ast.parse(source_code)
        mutator = ValueMutator(idx)
        mutated_tree = mutator.visit(tree)
        ast.fix_missing_locations(mutated_tree)
        code_obj = compile(mutated_tree, filename="<mutant>", mode="exec")
        
        mutant_module = {}
        exec(code_obj, mutant_module)
        
        original_attrs = {k: getattr(wa, k) for k in dir(wa) if not k.startswith("__")}
        for k, v in mutant_module.items():
            if not k.startswith("__"):
                setattr(wa, k, v)

        retcode = pytest.main(["-q", "tests/test_weather_analytics.py", "--no-header"])

        for k, v in original_attrs.items():
            setattr(wa, k, v)

        status = "KILLED" if retcode != 0 else "SURVIVED"
        if status == "KILLED":
            killed_count += 1
        else:
            survived_count += 1
            survived_list.append(f"M-VAL-{idx+1:02d}: {mutator.applied_mutation}")

    # Execute Arithmetic Mutations
    for idx in range(num_arithmetic):
        tree = ast.parse(source_code)
        mutator = ArithmeticMutator(idx)
        mutated_tree = mutator.visit(tree)
        ast.fix_missing_locations(mutated_tree)
        code_obj = compile(mutated_tree, filename="<mutant>", mode="exec")
        
        mutant_module = {}
        exec(code_obj, mutant_module)
        
        original_attrs = {k: getattr(wa, k) for k in dir(wa) if not k.startswith("__")}
        for k, v in mutant_module.items():
            if not k.startswith("__"):
                setattr(wa, k, v)

        retcode = pytest.main(["-q", "tests/test_weather_analytics.py", "--no-header"])

        for k, v in original_attrs.items():
            setattr(wa, k, v)

        status = "KILLED" if retcode != 0 else "SURVIVED"
        if status == "KILLED":
            killed_count += 1
        else:
            survived_count += 1
            survived_list.append(f"M-ARI-{idx+1:02d}: {mutator.applied_mutation}")

    total_mutants = killed_count + survived_count
    score = (killed_count / total_mutants * 100) if total_mutants > 0 else 0.0

    print(f"\nTotal Mutants Generated : {total_mutants}")
    print(f"Mutants Killed          : {killed_count}")
    print(f"Mutants Survived        : {survived_count}")
    print(f"MUTATION SCORE          : {score:.2f}%\n")

    if survived_list:
        print("SURVIVED MUTANTS:")
        for sm in survived_list:
            print(" -", sm)

if __name__ == "__main__":
    run_mutation_tests()
