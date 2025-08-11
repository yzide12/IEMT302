# Music Prediction Model Development Prompt

## Project Overview
Develop a machine learning model that can predict various aspects of music based on audio features and metadata. This model should be capable of making predictions about music characteristics, user preferences, or music-related outcomes.

## Model Objectives
Create a predictive model that can:
- Predict music genre classification
- Forecast music popularity/success metrics
- Predict user music preferences
- Estimate music mood/emotion
- Predict music recommendation scores

## Training Data Requirements

### Data Sources
1. **Audio Features Dataset**
   - Spotify API data (acousticness, danceability, energy, instrumentalness, etc.)
   - Last.fm API data (tags, play counts, user ratings)
   - MusicBrainz metadata (artist info, album details, release dates)
   - User listening history and behavior data

### Data Structure
- **Minimum Dataset Size**: 10,000+ music tracks
- **Data Format**: CSV, JSON, or database format
- **Time Period**: Historical data spanning 2-5 years
- **Update Frequency**: Monthly or quarterly data refreshes

### Data Quality Requirements
- Clean, normalized audio features
- Consistent metadata across sources
- Balanced representation across genres
- Minimal missing values (<5%)
- Validated user behavior data

## Features (Input Variables)

### Audio Features (Numerical)
- **Rhythm Features**: tempo, beats_per_minute, time_signature
- **Spectral Features**: spectral_centroid, spectral_bandwidth, spectral_rolloff
- **MFCC Features**: 13-20 Mel-frequency cepstral coefficients
- **Harmonic Features**: harmonic_percent, inharmonic_percent
- **Perceptual Features**: loudness, pitch, timbre characteristics

### Metadata Features (Categorical/Numerical)
- **Artist Information**: artist_popularity, artist_genre, artist_followers
- **Track Information**: release_year, album_type, track_number
- **Cultural Features**: language, country_of_origin, cultural_influence_score
- **Commercial Features**: label, budget, marketing_spend

### User Behavior Features
- **Listening Patterns**: play_count, skip_rate, repeat_listen_ratio
- **Social Features**: shares, comments, playlist_additions
- **Temporal Features**: time_of_day, day_of_week, seasonal_trends
- **Contextual Features**: listening_device, location, activity_type

### Derived Features
- **Feature Interactions**: tempo × energy, loudness × danceability
- **Statistical Aggregations**: rolling averages, trend indicators
- **Normalized Scores**: z-scores, min-max scaling, percentile ranks

## Labels (Target Variables)

### Primary Prediction Targets
1. **Genre Classification** (Multi-class)
   - Rock, Pop, Hip-Hop, Electronic, Classical, Jazz, Country, etc.
   - Confidence scores for each genre

2. **Popularity Prediction** (Regression)
   - Stream count predictions
   - Chart position forecasting
   - Viral potential scoring

3. **User Preference Score** (Regression)
   - 0-100 preference rating
   - Like/dislike probability
   - Recommendation strength

4. **Mood/Emotion Classification** (Multi-class)
   - Happy, Sad, Energetic, Calm, Aggressive, Melancholic
   - Emotion intensity scores

### Secondary Targets
- **Danceability Score** (0-1 scale)
- **Energy Level** (0-1 scale)
- **Acousticness** (0-1 scale)
- **Instrumentalness** (0-1 scale)

## Expected Outputs

### Model Predictions
1. **Primary Predictions**
   - Predicted genre with confidence scores
   - Popularity metrics with prediction intervals
   - User preference scores with uncertainty bounds
   - Mood classification with emotion mapping

2. **Prediction Confidence**
   - Confidence intervals for regression outputs
   - Probability distributions for classification
   - Uncertainty quantification metrics

3. **Feature Importance**
   - Feature ranking by predictive power
   - SHAP values for model interpretability
   - Feature interaction effects

### Model Performance Metrics
- **Classification Metrics**: Accuracy, Precision, Recall, F1-Score, ROC-AUC
- **Regression Metrics**: MAE, RMSE, R², MAPE
- **Cross-validation**: K-fold validation scores
- **Generalization**: Train vs. test performance comparison

### Deployment Outputs
- **API Endpoints**: RESTful API for real-time predictions
- **Batch Processing**: Bulk prediction capabilities
- **Model Monitoring**: Performance tracking and drift detection
- **A/B Testing**: Model comparison and validation

## Technical Requirements

### Model Architecture
- **Algorithm Selection**: Gradient Boosting (XGBoost, LightGBM), Neural Networks, or Ensemble methods
- **Model Complexity**: Balance between performance and interpretability
- **Scalability**: Handle 1000+ predictions per second
- **Latency**: <100ms response time for real-time predictions

### Data Pipeline
- **Feature Engineering**: Automated feature creation and selection
- **Data Preprocessing**: Normalization, encoding, handling missing values
- **Model Training**: Automated hyperparameter tuning
- **Model Deployment**: CI/CD pipeline for model updates

### Evaluation Framework
- **Holdout Validation**: 70% train, 15% validation, 15% test split
- **Cross-validation**: 5-fold cross-validation for robust evaluation
- **Business Metrics**: Alignment with business objectives
- **Model Interpretability**: Explainable AI requirements

## Success Criteria
- **Accuracy**: >85% for classification tasks, R² >0.8 for regression
- **Generalization**: <5% performance drop between train and test sets
- **Business Impact**: Measurable improvement in music recommendation quality
- **User Satisfaction**: Increased user engagement and retention metrics

## Deliverables
1. **Trained Model**: Production-ready model file
2. **API Service**: RESTful prediction service
3. **Documentation**: Model architecture and usage guide
4. **Performance Report**: Comprehensive evaluation results
5. **Deployment Guide**: Production deployment instructions
