# Comprehensive Paper Analysis Report

## Overview
This report presents a deep analysis of paper findings, aligned with the PRISMA flow diagram. The analysis aggregates data from multiple sources (Google Scholar, PubMed, Scopus, ArXiv), simulates the screening process, and analyzes papers that were potentially excluded.

## 1. Data Aggregation
We aggregated data from **19 CSV files** located in `source/dataset/useage/`.
- **Total Raw Records**: 13,327
- **Breakdown by Source**:
    - **ArXiv**: 6,939
    - **Google Scholar**: 3,545
    - **PubMed**: 1,678
    - **Scopus**: 1,165

## 2. PRISMA Flow Simulation
- **Identification**: 13,327 records identified.
- **Deduplication**: After normalizing titles (lowercase, alphanumeric only), we identified **2,851 duplicates**.
- **Unique Records**: 10,476 unique papers remained for screening.

### Source Overlap
A Venn diagram was generated (`venn_diagram.png`) to visualize the overlap between the top data sources. This helps understand if sources are providing unique or redundant content.

## 3. Missing Paper Analysis (Exclusion)
We compared the unique papers against the `finalized_papers.bib` file (which contains 20 included studies).
- **Missing/Excluded Papers**: **10,463** papers were present in the search results but not in the finalized list.

### Potential Reasons for Exclusion
We analyzed the titles of these missing papers to infer potential reasons for exclusion based on the PRISMA diagram criteria:
- **Chinese Traditional Medicine**: ~138 papers contained keywords like "Chinese", "Traditional Medicine", "Herbal", "Acupuncture".
- **Non-Empirical / Reviews**: ~1,675 papers were identified as "Review", "Survey", "Overview", or "Meta-analysis".

*See `exclusion_reasons.png` for a visual breakdown.*

## 4. Keyword Trends (2020-2025)
We analyzed the prevalence of specific keywords in the titles of unique papers over time.
- **Keywords**: Transformer, BERT, GPT, Attention Mechanism.
- **Trends**: The usage of these terms has evolved, with "Transformer" and "BERT" showing strong presence, and "GPT" likely showing a sharp rise in recent years (2023-2025).

*See `keyword_trends.png` for the trend line chart.*

## 5. Output Files
- **`deep_paper_analysis.ipynb`**: The Jupyter Notebook containing all code and visualizations.
- **`comprehensive_missing_papers_analysis.csv`**: A detailed CSV list of all 10,463 missing papers, including flags for potential exclusion reasons (`Is_CTM`, `Is_Review`).
- **Images**:
    - `venn_diagram.png`
    - `exclusion_reasons.png`
    - `keyword_trends.png`
