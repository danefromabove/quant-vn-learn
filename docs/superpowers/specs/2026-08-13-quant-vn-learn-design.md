# Quant VN Learn — Design Specification

**Date:** 2026-08-13
**Author:** Claude (AI Assistant)
**Purpose:** Learning quantitative finance from zero — Vietnamese equities focus

---

## 1. Mục tiêu & Triết lý

### 1.1 Mục tiêu chính
- Xây dựng nền tảng quant từ số 0
- Hiểu sâu, không chỉ biết làm
- Thỏa mãn trí tuệ

### 1.2 Triết lý học tập
| Triết lý | Áp dụng |
|----------|---------|
| **Learning by doing** | Mỗi concept đi kèm hands-on project |
| **Statistical rigor sớm** | Biases, p-hacking từ đầu — tránh养成习惯 sai |
| **Vietnam context** | Dữ liệu VN, không phải US textbook examples |
| **Production mindset** | Clean code, reproducibility ngay từ đầu |
| **Progressive complexity** | Từ đơn giản → phức tạp, mỗi bước vững chắc |
| **Bilingual** | Giải thích bằng tiếng Việt + English |

---

## 2. Lộ trình 5 Phase

```
Phase 1: Nền tảng (1-2 tháng)
Phase 2: Dữ liệu + Phân tích (1-2 tháng)
Phase 3: Quant Cơ bản (2-3 tháng)
Phase 4: Quant Chuyên sâu (3-4 tháng)
Phase 5: Research + Production (ongoing)
```

---

## 3. Phase 1: Nền tảng

### 3.1 Mục tiêu
- Python fluency cho data science
- Hiểu tài chính cơ bản (stocks, returns, markets)
- Nền tảng thống kê và xác suất

### 3.2 Cấu trúc thư mục

```
phase1-fundamentals/
├── README.md
├── notebooks/
│   ├── 01-python-essentials.ipynb
│   ├── 02-numpy-pandas.ipynb
│   ├── 03-data-visualization.ipynb
│   ├── 04-statistics-basics.ipynb
│   ├── 05-probability.ipynb
│   └── 06-finance-basics.ipynb
├── scripts/
│   ├── setup_environment.py
│   ├── data_types_demo.py
│   └── stats_demo.py
└── projects/
    └── project1-data-exploration-vn.ipynb
```

### 3.3 Nội dung chi tiết

#### 3.3.1 Python Essentials
- Variables, data types, operators
- Control flow (if/else, loops)
- Functions, lambda
- List, dict, set comprehensions
- File I/O, JSON handling
- **Project:** Viết script đọc file CSV VN stock data

#### 3.3.2 NumPy & Pandas
- NumPy arrays, broadcasting, vectorization
- Pandas Series, DataFrame
- Indexing, slicing, filtering
- GroupBy, merge, pivot
- Handling missing data
- **Project:** Clean và analyze sample VN stock data

#### 3.3.3 Data Visualization
- Matplotlib basics (line, bar, scatter)
- Seaborn (statistical plots)
- Plotly interactive charts
- Time series visualization
- **Project:** Visualize VN stock price history

#### 3.3.4 Statistics Basics
- Descriptive statistics (mean, median, std, skew, kurtosis)
- Distributions (normal, t, binomial)
- Hypothesis testing (t-test, chi-square)
- Confidence intervals
- Correlation, covariance
- **Project:** Analyze return distribution of VN stocks

#### 3.3.5 Probability
- Probability basics
- Bayes theorem
- Random variables
- Law of large numbers, Central limit theorem
- **Project:** Simulate stock price paths (random walk)

#### 3.3.6 Finance Basics
- What is a stock?
- What is a market? (HOSE, HNX)
- Returns (simple, log), volatility
- Risk vs. return
- Market indices (VN-Index, HNX-Index)
- **Project:** Calculate returns for top VN stocks

### 3.4 Output artifacts
- [ ] 6 Jupyter notebooks (learning)
- [ ] 3 Python scripts (production-ready)
- [ ] 1 project notebook
- [ ] Summary report (What I learned)

---

## 4. Phase 2: Dữ liệu + Phân tích

### 4.1 Mục tiêu
- Thu thập và clean dữ liệu VN
- Exploratory Data Analysis (EDA)
- Feature engineering basics
- Data quality assessment

### 4.2 Cấu trúc thư mục

```
phase2-data-analysis/
├── README.md
├── notebooks/
│   ├── 01-vn-data-sources.ipynb
│   ├── 02-data-collection.ipynb
│   ├── 03-data-cleaning.ipynb
│   ├── 04-eda-vn-stocks.ipynb
│   └── 05-feature-engineering.ipynb
├── scripts/
│   ├── collectors/
│   │   ├── cafef_collector.py
│   │   ├── vnd_collector.py
│   │   └── tcbs_collector.py
│   ├── cleaners/
│   │   └── data_cleaner.py
│   └── utils/
│       ├── date_utils.py
│       └── stock_utils.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
└── projects/
    └── project2-vn-stock-eda.ipynb
```

### 4.3 Nội dung chi tiết

#### 4.3.1 VN Data Sources
- Cafef.vn (historical prices, financials)
- VND (VNDirect)
- TCBS (Tiger Chart)
- SSI, FPS data feeds
- Limitations của data VN
- **Hands-on:** Explore each source

#### 4.3.2 Data Collection
- Web scraping basics (requests, BeautifulSoup)
- API consumption
- Rate limiting, error handling
- Scheduling data pulls
- **Project:** Build simple data collector

#### 4.3.3 Data Cleaning
- Handling missing values
- Outlier detection
- Data type conversions
- Time zone handling
- Survivorship bias awareness
- **Project:** Clean dirty VN stock dataset

#### 4.3.4 EDA - VN Stocks
- Distribution analysis
- Correlation patterns
- Sector analysis
- Time series patterns
- **Project:** Full EDA on VN stock universe

#### 4.3.5 Feature Engineering
- Price-based features (returns, volatility)
- Technical indicators
- Calendar features (day of week, month)
- **Project:** Create features for future modeling

### 4.4 Output artifacts
- [ ] 5 Jupyter notebooks
- [ ] Data collection scripts
- [ ] Cleaned VN stock dataset
- [ ] EDA report

---

## 5. Phase 3: Quant Cơ bản

### 5.1 Mục tiêu
- Hiểu factor investing
- Simple factor research
- Backtesting fundamentals
- Tránh common pitfalls

### 5.2 Cấu trúc thư mục

```
phase3-quant-basics/
├── README.md
├── notebooks/
│   ├── 01-intro-to-factors.ipynb
│   ├── 02-momentum-factors.ipynb
│   ├── 03-value-factors.ipynb
│   ├── 04-size-factors.ipynb
│   ├── 05-quality-factors.ipynb
│   ├── 06-backtesting-basics.ipynb
│   └── 07-common-pitfalls.ipynb
├── scripts/
│   ├── factors/
│   │   ├── momentum.py
│   │   ├── value.py
│   │   └── quality.py
│   ├── backtester/
│   │   ├── engine.py
│   │   └── portfolio.py
│   └── analysis/
│       └── performance.py
├── projects/
│   └── project3-simple-factor-backtest.ipynb
└── papers/
    └── paper1-factor-introduction.md
```

### 5.3 Nội dung chi tiết

#### 5.3.1 Intro to Factors
- What is a factor?
- Alpha vs. beta
- Factor zoo introduction
- Risk factors vs. alpha factors
- **Concept:** Fama-French framework

#### 5.3.2 Momentum Factors
- Price momentum (12-month, 1-month)
- Reversal (short-term)
- Implementation
- **Hands-on:** Calculate momentum for VN stocks

#### 5.3.3 Value Factors
- P/E, P/B, P/S ratios
- EV/EBITDA
- Dividend yield
- **Hands-on:** Calculate value scores

#### 5.3.4 Size Factors
- Market cap
- Small vs. large cap
- Size premium discussion

#### 5.3.5 Quality Factors
- ROE, ROA
- Debt-to-equity
- Gross margin
- **Hands-on:** Calculate quality scores

#### 5.3.6 Backtesting Basics
- What is backtesting?
- Simple backtest framework
- Portfolio construction
- Performance metrics ( Sharpe, IR)
- **Project:** Simple momentum backtest

#### 5.3.7 Common Pitfalls
- Look-ahead bias
- Survivorship bias
- Transaction costs
- Overfitting
- Data snooping
- **Concept:** Why VN is challenging

### 5.4 Output artifacts
- [ ] 7 Jupyter notebooks
- [ ] Factor calculation scripts
- [ ] Simple backtester
- [ ] Research paper (Factor Introduction)
- [ ] Backtest report

---

## 6. Phase 4: Quant Chuyên sâu

### 6.1 Mục tiêu
- Multi-factor models
- Portfolio optimization
- Advanced statistics
- Risk management
- Vietnam-specific considerations

### 6.2 Cấu trúc thư mục

```
phase4-advanced-quant/
├── README.md
├── notebooks/
│   ├── 01-multi-factor-models.ipynb
│   ├── 02-factor-risk-model.ipynb
│   ├── 03-portfolio-optimization.ipynb
│   ├── 04-risk-management.ipynb
│   ├── 05-statistical-testing.ipynb
│   ├── 06-cross-validation.ipynb
│   ├── 07-vn-specific-challenges.ipynb
│   └── 08-factor-decay-survivorship.ipynb
├── scripts/
│   ├── models/
│   │   ├── risk_model.py
│   │   └── optimizer.py
│   ├── risk/
│   │   └── risk_metrics.py
│   └── testing/
│       └── statistical_tests.py
├── projects/
│   └── project4-multi-factor-portfolio.ipynb
└── papers/
    ├── paper2-multi-factor-model.md
    └── paper3-vn-market-analysis.md
```

### 6.3 Nội dung chi tiết

#### 6.3.1 Multi-Factor Models
- Combining factors
- Factor correlation
- Factor orthogonalization
- Weighted combination
- **Project:** Build 3-factor model for VN

#### 6.3.2 Factor Risk Model
- Covariance estimation
- Factor exposures
- Risk attribution
- **Concept:** Barra risk model basics

#### 6.3.3 Portfolio Optimization
- Mean-variance optimization
- Black-Litterman
- Risk parity
- Constraint handling
- **Project:** Optimize VN portfolio

#### 6.3.4 Risk Management
- VaR, CVaR
- Drawdown analysis
- Position sizing
- Leverage considerations
- **Hands-on:** Risk report for VN portfolio

#### 6.3.5 Statistical Testing
- Multiple testing problem
- Bootstrap
- Walk-forward analysis
- Out-of-sample testing
- **Concept:** Deflated Sharpe Ratio

#### 6.3.6 Cross-Validation for Time Series
- Purged K-Fold
- Embargo
- Combinatorial purged cross-validation
- Why random CV fails for time series

#### 6.3.7 VN-Specific Challenges
- Limited history
- Delisted stocks
- Illiquidity
- Ownership structure
- Related party transactions
- **Concept:** How to handle VN data limitations

#### 6.3.8 Factor Decay & Survivorship
- Why factors decay
- Survivorship bias in VN
- Live tracking vs. backtest
- **Project:** Factor decay analysis

### 6.4 Output artifacts
- [ ] 8 Jupyter notebooks
- [ ] Risk model & optimizer
- [ ] Statistical testing framework
- [ ] 2 research papers
- [ ] Full backtest report

---

## 7. Phase 5: Research + Production

### 7.1 Mục tiêu
- Research methodology
- Writing quant research papers
- Production code practices
- Reproducibility

### 7.2 Cấu trúc thư mục

```
phase5-research-production/
├── README.md
├── notebooks/
│   ├── 01-research-methodology.ipynb
│   ├── 02-paper-writing.ipynb
│   └── 03-code-review.ipynb
├── scripts/
│   ├── research/
│   │   ├── hypothesis_testing.py
│   │   └── results_reporting.py
│   ├── production/
│   │   ├── logging.py
│   │   ├── config.py
│   │   └── testing.py
│   └── reproducibility/
│       ├── experiment_tracker.py
│       └── data_versioning.py
├── templates/
│   ├── research-paper-template.md
│   └── experiment-template.md
└── projects/
    └── project5-capstone-research.ipynb
```

### 7.3 Nội dung chi tiết

#### 7.3.1 Research Methodology
- Hypothesis-driven research
- Literature review
- Experiment design
- Results interpretation
- **Concept:** Scientific method in quant

#### 7.3.2 Paper Writing
- Structure of quant paper
- Results presentation
- Table and figure guidelines
- Academic writing style
- **Project:** Write research paper on VN factor

#### 7.3.3 Production Code Practices
- Code review
- Testing (unit, integration)
- Documentation
- Logging
- Error handling
- **Hands-on:** Refactor previous code

#### 7.3.4 Reproducibility
- Version control (git)
- Data versioning
- Experiment tracking
- Environment reproducibility
- **Concept:** MLflow, DVC basics

### 7.4 Output artifacts
- [ ] 3 Jupyter notebooks
- [ ] Production-ready scripts
- [ ] Research paper template
- [ ] Capstone research project
- [ ] Final thesis/report

---

## 8. Technical Stack

### 8.1 Core Dependencies
```
python>=3.13
jupyter>=1.0
numpy>=1.26
pandas>=2.1
scipy>=1.11
matplotlib>=3.8
seaborn>=0.13
plotly>=5.18
scikit-learn>=1.4
statsmodels>=0.14
```

### 8.2 Quant-Specific
```
arch>=6.0  # volatility modeling
pyfolio>=0.9  # portfolio analysis (deprecated, use own impl)
empyrical>=0.5  # risk metrics
```

### 8.3 Data
```
pandas-datareader>=0.10
yfinance>=0.2
requests>=2.31
beautifulsoup4>=4.12
```

### 8.4 Development
```
pytest>=7.4
black>=24.0
ruff>=0.1
mypy>=1.7
```

---

## 9. Project Structure (Root)

```
quant-vn-learn/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── requirements.txt
├── environment.yml
├── phase1-fundamentals/
├── phase2-data-analysis/
├── phase3-quant-basics/
├── phase4-advanced-quant/
├── phase5-research-production/
├── docs/
│   ├── reading-list.md
│   ├── resources.md
│   └── superpowers/
│       └── specs/
├── .github/
│   └── workflows/
│       └── tests.yml
└── .gitignore
```

---

## 10. Reading List

### Essentials
1. "Quantitative Investing" —坛
2. "Advances in Financial Machine Learning" — Marcos López de Prado
3. "Evidence-Based Technical Analysis" — David Aronson
4. "Machine Learning for Asset Managers" — Marcos López de Prado

### Statistics
1. "Think Stats" — Allen Downey
2. "Statistical Consequences of Fat Tails" — Nassim Taleb

### Finance
1. "Investments" — Bodie, Kane, Marcus
2. "A Random Walk Down Wall Street" — Burton Malkiel

### Vietnam
1. Các báo cáo từ BVSC, SSI, VNDirect
2. UBCKNN (State Securities Commission) reports

---

## 11. Success Criteria

### Phase 1-2 (Foundation)
- [ ] Python fluently for data tasks
- [ ] Collect and clean VN stock data
- [ ] Perform EDA independently

### Phase 3 (Quant Basics)
- [ ] Understand factor investing
- [ ] Run simple backtest
- [ ] Identify common pitfalls

### Phase 4 (Advanced)
- [ ] Build multi-factor model
- [ ] Optimize portfolio
- [ ] Handle VN-specific challenges

### Phase 5 (Research)
- [ ] Write research paper
- [ ] Production-ready code
- [ ] Reproducible experiments

---

## 12. Next Steps

1. **Immediate:** Setup development environment
2. **Week 1-2:** Complete Phase 1.1-1.3 (Python essentials)
3. **Week 3-4:** Complete Phase 1.4-1.6 (Stats + Finance)
4. **Ongoing:** Phase 2 data infrastructure
5. **Monthly:** Review and adjust pace

---

*Document status: Draft*
*Last updated: 2026-08-13*
