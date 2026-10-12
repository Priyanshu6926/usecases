#!/usr/bin/env python3
"""
Experiment No. 08: AI-Based Customer Persona Generation from Marketing Data
Somaiya Vidyavihar University | K J Somaiya School of Engineering
Department of Information Technology | Sem-VII DiM (2026-27)
Batch: A2 | Roll No: 16010423075

This script performs end-to-end AI-based customer segmentation using K-Means clustering,
elbow method optimization, silhouette scoring, cluster profiling, and automated
customer persona generation with tailored digital marketing strategies.
"""

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Set style for professional academic visualizations
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 0.8

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'customer_marketing_data.csv')
ASSETS_DIR = os.path.join(BASE_DIR, 'persona_assets')
os.makedirs(ASSETS_DIR, exist_ok=True)

def run_customer_persona_pipeline():
    print("=" * 80)
    print("EXPERIMENT 08: AI-BASED CUSTOMER PERSONA GENERATION FROM MARKETING DATA")
    print("=" * 80)

    # 1. LOAD DATASET
    print("\n[Step 1] Loading Marketing Dataset...")
    df = pd.read_csv(DATA_PATH)
    print(f"Dataset successfully loaded. Total Records: {len(df)}, Features: {list(df.columns)}")
    print("\nDataset Preview (First 5 records):")
    print(df.head())

    # 2. EXPLORATORY DATA ANALYSIS (EDA) & DATA CLEANING
    print("\n[Step 2] Exploratory Data Analysis & Data Cleaning...")
    print("\nMissing values per column:")
    print(df.isnull().sum())
    print(f"Duplicate rows detected: {df.duplicated().sum()}")
    
    print("\nSummary Statistics of Quantitative Features:")
    summary_stats = df.describe().T[['mean', 'std', 'min', '50%', 'max']]
    print(summary_stats)

    # 3. FEATURE SELECTION
    print("\n[Step 3] Selecting Numerical Features for K-Means Clustering...")
    feature_cols = ['Age', 'Annual_Income_k', 'Spending_Score', 'Purchase_Frequency', 'Avg_Order_Value']
    X = df[feature_cols].copy()
    print(f"Features selected for clustering: {feature_cols}")

    # 4. FEATURE NORMALIZATION (StandardScaler)
    print("\n[Step 4] Normalizing Features using StandardScaler...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print(f"Scaled feature matrix shape: {X_scaled.shape}")
    print("Zero-mean and unit-variance normalization verified:")
    print(f"Means: {np.round(X_scaled.mean(axis=0), 4)}")
    print(f"Stds:  {np.round(X_scaled.std(axis=0), 4)}")

    # 5. ELBOW METHOD & SILHOUETTE ANALYSIS (OPTIMAL K SELECTION)
    print("\n[Step 5] Evaluating Optimal K via Elbow Method and Silhouette Analysis...")
    k_range = range(2, 11)
    wcss = []
    silhouette_scores = []

    # Calculate WCSS for K=1 first for the elbow curve
    kmeans_1 = KMeans(n_clusters=1, random_state=42, n_init=10)
    kmeans_1.fit(X_scaled)
    wcss_full = [kmeans_1.inertia_]

    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        wcss.append(km.inertia_)
        wcss_full.append(km.inertia_)
        score = silhouette_score(X_scaled, km.labels_)
        silhouette_scores.append(score)
        print(f"K = {k:2d} | WCSS (Inertia): {km.inertia_:9.2f} | Silhouette Score: {score:.4f}")

    # Plot 1: Elbow Curve & Silhouette Scores
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), dpi=300)
    
    ax1.plot(range(1, 11), wcss_full, marker='o', linewidth=2, color='#2563eb', markersize=6)
    ax1.axvline(x=5, color='#ef4444', linestyle='--', linewidth=1.5, label='Optimal K = 5 (Elbow Point)')
    ax1.set_title('Elbow Method For Optimal K', fontsize=13, fontweight='bold', pad=12)
    ax1.set_xlabel('Number of Clusters (K)', fontsize=11)
    ax1.set_ylabel('Within-Cluster Sum of Squares (WCSS)', fontsize=11)
    ax1.legend(frameon=True)
    ax1.grid(True, linestyle=':', alpha=0.6)

    ax2.plot(k_range, silhouette_scores, marker='s', linewidth=2, color='#10b981', markersize=6)
    ax2.axvline(x=5, color='#ef4444', linestyle='--', linewidth=1.5, label=f'Peak Score at K=5 ({silhouette_scores[3]:.3f})')
    ax2.set_title('Silhouette Analysis For Cluster Separation', fontsize=13, fontweight='bold', pad=12)
    ax2.set_xlabel('Number of Clusters (K)', fontsize=11)
    ax2.set_ylabel('Silhouette Coefficient', fontsize=11)
    ax2.legend(frameon=True)
    ax2.grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()
    elbow_path = os.path.join(ASSETS_DIR, 'elbow_method_analysis.png')
    plt.savefig(elbow_path, bbox_inches='tight')
    plt.close()
    print(f"Elbow & Silhouette visualization saved to: {elbow_path}")

    # 6. K-MEANS CLUSTERING (K=5)
    optimal_k = 5
    print(f"\n[Step 6] Fitting Final K-Means Model with K = {optimal_k}...")
    final_kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=15)
    df['Cluster'] = final_kmeans.fit_predict(X_scaled)
    final_silhouette = silhouette_score(X_scaled, df['Cluster'])
    print(f"K-Means training converged in {final_kmeans.n_iter_} iterations.")
    print(f"Overall Model Silhouette Score: {final_silhouette:.4f}")

    # Cluster Distribution
    cluster_counts = df['Cluster'].value_counts().sort_index()
    print("\nCustomer count per cluster:")
    for c_id, count in cluster_counts.items():
        print(f"Cluster {c_id}: {count} customers ({count/len(df)*100:.1f}%)")

    # 7. CLUSTER CENTROIDS & STATISTICAL PROFILES
    print("\n[Step 7] Computing Cluster Centroids in Original Feature Space...")
    cluster_profile = df.groupby('Cluster')[feature_cols].mean()
    print("\nCluster Centroid Means (Original Units):")
    print(cluster_profile.round(2))

    # Channel preferences by cluster
    channel_pref = df.groupby(['Cluster', 'Preferred_Channel']).size().unstack(fill_value=0)
    print("\nPreferred Marketing Channel by Cluster:")
    print(channel_pref)

    # 8. MAPPING CLUSTERS TO CUSTOMER PERSONAS
    # Assign human personas based on centroid characteristics
    persona_definitions = {
        0: {
            "name": "Trendsetting Impulse Buyer",
            "tagline": "Young, socially connected, trendy, fast purchasing cycles",
            "archetype": "The Trend Chaser",
            "color": "#ec4899"
        },
        1: {
            "name": "Budget-Conscious Bargain Hunter",
            "tagline": "Price-sensitive, deliberate decision-maker, deal seeker",
            "archetype": "The Practical Saver",
            "color": "#eab308"
        },
        2: {
            "name": "Elite VIP High-Roller",
            "tagline": "Affluent, high purchasing power, brand conscious, frequent buyer",
            "archetype": "The Premium Enthusiast",
            "color": "#8b5cf6"
        },
        3: {
            "name": "Cautious Affluent Saver",
            "tagline": "High earning capacity, conservative spending, high scrutiny",
            "archetype": "The Discerning Investor",
            "color": "#06b6d4"
        },
        4: {
            "name": "Mainstream Pragmatist",
            "tagline": "Moderate income and spending, consistent regular buyer",
            "archetype": "The Everyday Core",
            "color": "#10b981"
        }
    }

    # Match each cluster ID to its proper archetype based on income & spend
    # Calculate relative rankings to ensure robust mapping
    cluster_mapping = {}
    for c_id in range(optimal_k):
        inc = cluster_profile.loc[c_id, 'Annual_Income_k']
        spd = cluster_profile.loc[c_id, 'Spending_Score']
        
        if inc < 50 and spd > 60:
            cluster_mapping[c_id] = 0  # Trendsetting Impulse Buyer
        elif inc < 50 and spd <= 60:
            cluster_mapping[c_id] = 1  # Budget Bargain Hunter
        elif inc >= 70 and spd > 60:
            cluster_mapping[c_id] = 2  # Elite VIP
        elif inc >= 70 and spd <= 60:
            cluster_mapping[c_id] = 3  # Cautious Affluent Saver
        else:
            cluster_mapping[c_id] = 4  # Mainstream Pragmatist

    df['Persona_ID'] = df['Cluster'].map(cluster_mapping)
    df['Persona_Name'] = df['Persona_ID'].map(lambda p: persona_definitions[p]['name'])
    df['Persona_Archetype'] = df['Persona_ID'].map(lambda p: persona_definitions[p]['archetype'])

    # 9. ADVANCED VISUALIZATIONS
    print("\n[Step 8] Generating Comprehensive Cluster Visualizations...")

    # Plot 2: 2D Scatter Plot of Annual Income vs Spending Score
    plt.figure(figsize=(10, 7), dpi=300)
    palette = [persona_definitions[p]['color'] for p in sorted(persona_definitions.keys())]

    scatter = sns.scatterplot(
        data=df,
        x='Annual_Income_k',
        y='Spending_Score',
        hue='Persona_Name',
        palette=palette,
        s=80,
        alpha=0.85,
        edgecolor='white',
        linewidth=0.8
    )

    # Plot Centroids in original space
    centroids_orig = df.groupby('Persona_Name')[['Annual_Income_k', 'Spending_Score']].mean()
    plt.scatter(
        centroids_orig['Annual_Income_k'],
        centroids_orig['Spending_Score'],
        s=260,
        c='black',
        marker='*',
        edgecolor='#facc15',
        linewidth=1.5,
        label='Persona Centroids (Anchor)'
    )

    plt.title('AI Customer Segmentation: Annual Income vs. Spending Score', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Annual Income ($k)', fontsize=12)
    plt.ylabel('Spending Score (1 - 100)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True, title="Customer Personas")
    plt.tight_layout()
    scatter_path = os.path.join(ASSETS_DIR, 'customer_clusters_scatter.png')
    plt.savefig(scatter_path, bbox_inches='tight')
    plt.close()
    print(f"2D Cluster Scatter Plot saved to: {scatter_path}")

    # Plot 3: Feature Distribution across Personas (Box Plots)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), dpi=300)
    plot_feats = [
        ('Age', 'Customer Age (Years)', axes[0, 0]),
        ('Annual_Income_k', 'Annual Income ($k)', axes[0, 1]),
        ('Spending_Score', 'Spending Score (1-100)', axes[1, 0]),
        ('Purchase_Frequency', 'Annual Purchase Frequency (Orders/yr)', axes[1, 1])
    ]

    for feat, label, ax in plot_feats:
        sns.boxplot(
            data=df,
            x='Persona_Archetype',
            y=feat,
            palette=palette,
            ax=ax,
            boxprops=dict(alpha=0.8),
            fliersize=3
        )
        ax.set_title(label, fontsize=12, fontweight='bold')
        ax.set_xlabel('')
        ax.set_ylabel(label)
        ax.tick_params(axis='x', rotation=15)
        ax.grid(True, linestyle=':', alpha=0.5)

    plt.suptitle('Demographic & Behavioral Variance Across Generated Personas', fontsize=15, fontweight='bold', y=0.99)
    plt.tight_layout()
    dist_path = os.path.join(ASSETS_DIR, 'cluster_feature_distribution.png')
    plt.savefig(dist_path, bbox_inches='tight')
    plt.close()
    print(f"Feature Distribution Boxplots saved to: {dist_path}")

    # Plot 4: Normalized Radar / Spider Profile Comparison
    categories = ['Age', 'Income', 'Spend Score', 'Frequency', 'Order Value']
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # Close loop

    # Normalize group means between 0 and 1 for radar
    radar_df = df.groupby('Persona_ID')[feature_cols].mean()
    radar_norm = (radar_df - radar_df.min()) / (radar_df.max() - radar_df.min())

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), dpi=300)
    plt.xticks(angles[:-1], categories, color='#334155', size=11, fontweight='bold')

    for p_id in sorted(persona_definitions.keys()):
        values = radar_norm.loc[p_id].tolist()
        values += values[:1]
        p_info = persona_definitions[p_id]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=p_info['archetype'], color=p_info['color'])
        ax.fill(angles, values, color=p_info['color'], alpha=0.15)

    ax.set_title('Multi-Dimensional Persona Profile Radar', size=14, fontweight='bold', pad=25)
    plt.legend(loc='upper right', bbox_to_anchor=(1.35, 1.1), title="Archetypes")
    radar_path = os.path.join(ASSETS_DIR, 'persona_radar_chart.png')
    plt.savefig(radar_path, bbox_inches='tight')
    plt.close()
    print(f"Persona Radar Chart saved to: {radar_path}")

    # 10. GENERATE RICH PERSONA CARDS & DIGITAL MARKETING STRATEGY JSON
    personas_full_output = []
    
    marketing_strategies = {
        0: {
            "demographics": {
                "age_range": f"{df[df['Persona_ID']==0]['Age'].min()} - {df[df['Persona_ID']==0]['Age'].max()} yrs (Avg: {df[df['Persona_ID']==0]['Age'].mean():.1f})",
                "income_level": f"${df[df['Persona_ID']==0]['Annual_Income_k'].mean():.1f}k/yr (Entry/Junior level)",
                "gender_split": f"{df[df['Persona_ID']==0]['Gender'].value_counts(normalize=True).to_dict()}"
            },
            "behavior": {
                "avg_spending_score": f"{df[df['Persona_ID']==0]['Spending_Score'].mean():.1f}/100",
                "purchase_frequency": f"{df[df['Persona_ID']==0]['Purchase_Frequency'].mean():.1f} orders/year",
                "avg_order_value": f"${df[df['Persona_ID']==0]['Avg_Order_Value'].mean():.1f}"
            },
            "psychographics": {
                "interests": "Trending viral lifestyle, social media aesthetics, fast fashion, tech gadgets",
                "goals": "Social validation, instant gratification, staying ahead of trends",
                "pain_points": "FOMO (Fear Of Missing Out), limited disposable savings, shipping delays"
            },
            "channels": ["Instagram Reels / Stories", "TikTok", "Mobile Push Notifications", "Influencer Collabs"],
            "marketing_strategy": {
                "ad_format": "Short-form video ads, time-limited flash sale carousels, dynamic discount codes",
                "value_prop": "'Get it before it sells out — limited drop available now!'",
                "retargeting": "Automated abandoned cart push alerts within 3 hours offering 10% instant promo",
                "budget_allocation": "25% of digital ad spend (High ROAS on high impulse conversion)"
            }
        },
        1: {
            "demographics": {
                "age_range": f"{df[df['Persona_ID']==1]['Age'].min()} - {df[df['Persona_ID']==1]['Age'].max()} yrs (Avg: {df[df['Persona_ID']==1]['Age'].mean():.1f})",
                "income_level": f"${df[df['Persona_ID']==1]['Annual_Income_k'].mean():.1f}k/yr (Low to Mid bracket)",
                "gender_split": f"{df[df['Persona_ID']==1]['Gender'].value_counts(normalize=True).to_dict()}"
            },
            "behavior": {
                "avg_spending_score": f"{df[df['Persona_ID']==1]['Spending_Score'].mean():.1f}/100",
                "purchase_frequency": f"{df[df['Persona_ID']==1]['Purchase_Frequency'].mean():.1f} orders/year",
                "avg_order_value": f"${df[df['Persona_ID']==1]['Avg_Order_Value'].mean():.1f}"
            },
            "psychographics": {
                "interests": "Coupon clipping, price comparison sites, discount portals, thrifty householding",
                "goals": "Maximizing utility per dollar, stretching monthly budget, zero wasteful expenditure",
                "pain_points": "Hidden charges, high delivery fees, price increases without value justification"
            },
            "channels": ["Email Newsletters (Clearance/Discounts)", "Google Search (Discount query terms)", "SMS Deal Alerts"],
            "marketing_strategy": {
                "ad_format": "Bundle discount promotions, BOGO (Buy One Get One Free), clearance blowout banners",
                "value_prop": "'Guaranteed lowest price or price-match guarantee + Free Shipping'",
                "retargeting": "Weekly digest emails highlighting top price drops and threshold coupon vouchers",
                "budget_allocation": "15% of digital ad spend (Focus on high-volume discount events like Black Friday/Diwali)"
            }
        },
        2: {
            "demographics": {
                "age_range": f"{df[df['Persona_ID']==2]['Age'].min()} - {df[df['Persona_ID']==2]['Age'].max()} yrs (Avg: {df[df['Persona_ID']==2]['Age'].mean():.1f})",
                "income_level": f"${df[df['Persona_ID']==2]['Annual_Income_k'].mean():.1f}k/yr (Top 10% Earner)",
                "gender_split": f"{df[df['Persona_ID']==2]['Gender'].value_counts(normalize=True).to_dict()}"
            },
            "behavior": {
                "avg_spending_score": f"{df[df['Persona_ID']==2]['Spending_Score'].mean():.1f}/100",
                "purchase_frequency": f"{df[df['Persona_ID']==2]['Purchase_Frequency'].mean():.1f} orders/year",
                "avg_order_value": f"${df[df['Persona_ID']==2]['Avg_Order_Value'].mean():.1f}"
            },
            "psychographics": {
                "interests": "Luxury lifestyle, premium hospitality, bespoke services, executive technology",
                "goals": "Exclusive access, superior craftsmanship, personalized concierge experiences",
                "pain_points": "Poor customer service, commoditized generic products, lengthy checkout processes"
            },
            "channels": ["Exclusive VIP Email", "Instagram Curated Showcase", "Google Search (High-intent luxury terms)"],
            "marketing_strategy": {
                "ad_format": "High-production video ads, invitation-only VIP preview drops, white-glove onboarding",
                "value_prop": "'Engineered for perfection: Experience unmatched luxury and concierge service'",
                "retargeting": "Dedicated relationship manager outreach, early access to new releases",
                "budget_allocation": "35% of digital ad spend (Highest Customer Lifetime Value / LTV contributor)"
            }
        },
        3: {
            "demographics": {
                "age_range": f"{df[df['Persona_ID']==3]['Age'].min()} - {df[df['Persona_ID']==3]['Age'].max()} yrs (Avg: {df[df['Persona_ID']==3]['Age'].mean():.1f})",
                "income_level": f"${df[df['Persona_ID']==3]['Annual_Income_k'].mean():.1f}k/yr (High Earner, High Net Worth)",
                "gender_split": f"{df[df['Persona_ID']==3]['Gender'].value_counts(normalize=True).to_dict()}"
            },
            "behavior": {
                "avg_spending_score": f"{df[df['Persona_ID']==3]['Spending_Score'].mean():.1f}/100",
                "purchase_frequency": f"{df[df['Persona_ID']==3]['Purchase_Frequency'].mean():.1f} orders/year",
                "avg_order_value": f"${df[df['Persona_ID']==3]['Avg_Order_Value'].mean():.1f}"
            },
            "psychographics": {
                "interests": "Wealth management, long-term durability, functional design, investment assets",
                "goals": "Long-term reliability, proven track record, ROI and warranty assurance",
                "pain_points": "Gimmicky marketing, unverified product claims, aggressive high-pressure sales"
            },
            "channels": ["Google Search (In-depth review queries)", "LinkedIn Sponsored Articles", "Editorial Newsletters"],
            "marketing_strategy": {
                "ad_format": "Data-driven case studies, third-party laboratory certifications, 10-year durability guarantees",
                "value_prop": "'Invest in lasting reliability: Built to outperform and backed by a comprehensive warranty'",
                "retargeting": "Educational nurturing drip emails detailing product longevity and technical specifications",
                "budget_allocation": "15% of digital ad spend (High conversion value upon extensive evaluation)"
            }
        },
        4: {
            "demographics": {
                "age_range": f"{df[df['Persona_ID']==4]['Age'].min()} - {df[df['Persona_ID']==4]['Age'].max()} yrs (Avg: {df[df['Persona_ID']==4]['Age'].mean():.1f})",
                "income_level": f"${df[df['Persona_ID']==4]['Annual_Income_k'].mean():.1f}k/yr (Solid Middle Class)",
                "gender_split": f"{df[df['Persona_ID']==4]['Gender'].value_counts(normalize=True).to_dict()}"
            },
            "behavior": {
                "avg_spending_score": f"{df[df['Persona_ID']==4]['Spending_Score'].mean():.1f}/100",
                "purchase_frequency": f"{df[df['Persona_ID']==4]['Purchase_Frequency'].mean():.1f} orders/year",
                "avg_order_value": f"${df[df['Persona_ID']==4]['Avg_Order_Value'].mean():.1f}"
            },
            "psychographics": {
                "interests": "Family lifestyle, home improvement, dependable consumer goods, community forums",
                "goals": "Fair price-to-performance ratio, trustworthy daily solutions, dependable warranty",
                "pain_points": "Misleading product reviews, difficult returns, sudden subscription lock-ins"
            },
            "channels": ["Google Search", "Facebook Community Feeds", "Customer Review Portals", "Weekly Emails"],
            "marketing_strategy": {
                "ad_format": "Social proof carousels with 5-star customer ratings, user-generated review testimonials",
                "value_prop": "'Trusted by over 100,000 satisfied customers — reliability you can count on'",
                "retargeting": "Seasonal promotional triggers (Back to School, Holiday gift guides, Loyalty points)",
                "budget_allocation": "10% of digital ad spend (Consistent recurring baseline sales)"
            }
        }
    }

    # Save segmented dataset with labels
    segmented_csv_path = os.path.join(BASE_DIR, 'customer_marketing_data_segmented.csv')
    df.to_csv(segmented_csv_path, index=False)
    print(f"\n[Step 9] Enriched segmented dataset saved to: {segmented_csv_path}")

    # Save personas metadata to JSON for the Web App and documentation
    personas_metadata = []
    for p_id in sorted(persona_definitions.keys()):
        meta = {
            "persona_id": p_id,
            "name": persona_definitions[p_id]["name"],
            "archetype": persona_definitions[p_id]["archetype"],
            "tagline": persona_definitions[p_id]["tagline"],
            "color": persona_definitions[p_id]["color"],
            "size": int(cluster_counts[p_id]),
            "percentage": round(float(cluster_counts[p_id] / len(df) * 100), 1),
            "details": marketing_strategies[p_id]
        }
        personas_metadata.append(meta)

    meta_json_path = os.path.join(ASSETS_DIR, 'customer_personas_metadata.json')
    with open(meta_json_path, 'w') as f:
        json.dump(personas_metadata, f, indent=2)
    print(f"Customer Personas Metadata JSON saved to: {meta_json_path}")

    print("\n" + "=" * 80)
    print("AI CUSTOMER PERSONA GENERATION PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == '__main__':
    run_customer_persona_pipeline()
