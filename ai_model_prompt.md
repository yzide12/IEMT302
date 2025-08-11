# AI Model Development Prompt

## Task 2: AI Model Development Prompt

### Overview
This document provides a comprehensive prompt template for developing various types of AI models based on last week's activity. The prompt is designed to be adaptable for different model types and use cases.

---

## Universal AI Model Development Prompt

### Primary Prompt Structure

```
You are an expert AI model developer tasked with creating a sophisticated machine learning model for [SPECIFIC DOMAIN/APPLICATION]. 

**Project Context:**
- Domain: [e.g., Natural Language Processing, Computer Vision, Predictive Analytics, Recommendation Systems]
- Application: [e.g., Sentiment Analysis, Object Detection, Sales Forecasting, Product Recommendations]
- Target Users: [e.g., Business Analysts, End Users, Developers, Researchers]

**Technical Requirements:**
- Model Type: [e.g., Neural Network, Transformer, CNN, RNN, Random Forest, SVM]
- Programming Language: [e.g., Python, R, JavaScript]
- Framework: [e.g., TensorFlow, PyTorch, Scikit-learn, Hugging Face]
- Performance Metrics: [e.g., Accuracy, Precision, Recall, F1-Score, RMSE, MAE]
- Deployment Environment: [e.g., Cloud, Edge, Mobile, Web Application]

**Data Specifications:**
- Data Type: [e.g., Text, Images, Numerical, Time Series, Structured/Unstructured]
- Data Size: [e.g., Small (<1K samples), Medium (1K-100K), Large (>100K)]
- Data Quality: [e.g., Clean, Requires Preprocessing, Missing Values, Imbalanced]
- Data Sources: [e.g., Public Datasets, Internal Data, API Feeds, User Generated]

**Functional Requirements:**
- Input Format: [e.g., Text strings, Image files, Numerical arrays, JSON objects]
- Output Format: [e.g., Classification labels, Numerical predictions, Text responses, Confidence scores]
- Real-time Processing: [Yes/No]
- Batch Processing: [Yes/No]
- API Integration: [Required/Optional]

**Performance Requirements:**
- Accuracy Target: [e.g., >90% accuracy]
- Speed Requirements: [e.g., <100ms response time]
- Scalability: [e.g., Handle 1000+ requests per minute]
- Resource Constraints: [e.g., Memory <2GB, CPU usage <50%]

**Ethical Considerations:**
- Bias Mitigation: [Required/Optional]
- Privacy Protection: [Required/Optional]
- Transparency: [Required/Optional]
- Fairness Metrics: [Required/Optional]

**Development Phases:**
1. Data Preprocessing and Feature Engineering
2. Model Architecture Design
3. Training and Validation
4. Hyperparameter Optimization
5. Model Evaluation and Testing
6. Deployment and Monitoring

**Deliverables:**
- Complete source code with documentation
- Model performance report
- API endpoints (if required)
- Deployment instructions
- Testing suite
- User documentation

Please provide a complete implementation that includes:
1. Data loading and preprocessing pipeline
2. Model architecture definition
3. Training loop with validation
4. Evaluation metrics and visualization
5. Model saving and loading functionality
6. Prediction/inference interface
7. Error handling and logging
8. Unit tests and integration tests
```

---

## Specialized Prompts for Different Model Types

### 1. Natural Language Processing (NLP) Model

```
Create a state-of-the-art NLP model for [SPECIFIC TASK] using transformer architecture.

**NLP Task:** [e.g., Text Classification, Named Entity Recognition, Question Answering, Text Generation, Sentiment Analysis, Language Translation]

**Model Architecture:**
- Base Model: [e.g., BERT, GPT, T5, RoBERTa, DistilBERT]
- Fine-tuning Strategy: [e.g., Full Fine-tuning, LoRA, Adapter Tuning, Prompt Tuning]
- Tokenization: [e.g., WordPiece, SentencePiece, BPE]

**Text Processing:**
- Maximum Sequence Length: [e.g., 512 tokens]
- Special Tokens: [e.g., [CLS], [SEP], [PAD], [MASK]]
- Text Cleaning: [e.g., Remove HTML, Lowercase, Remove Punctuation]

**Training Configuration:**
- Learning Rate: [e.g., 2e-5]
- Batch Size: [e.g., 16, 32, 64]
- Epochs: [e.g., 3-10]
- Optimizer: [e.g., AdamW, Adam]
- Loss Function: [e.g., CrossEntropyLoss, BCEWithLogitsLoss]
```

### 2. Computer Vision Model

```
Develop a computer vision model for [SPECIFIC TASK] using deep learning techniques.

**Vision Task:** [e.g., Image Classification, Object Detection, Image Segmentation, Face Recognition, Image Generation]

**Model Architecture:**
- Base Model: [e.g., ResNet, VGG, EfficientNet, YOLO, U-Net, GAN]
- Pre-trained Weights: [e.g., ImageNet, COCO, Custom]
- Transfer Learning: [Yes/No]

**Image Processing:**
- Input Size: [e.g., 224x224, 512x512, Variable]
- Color Channels: [e.g., RGB, Grayscale, RGBA]
- Data Augmentation: [e.g., Rotation, Flip, Zoom, Color Jitter]
- Normalization: [e.g., ImageNet stats, Custom range]

**Training Configuration:**
- Learning Rate: [e.g., 1e-4]
- Batch Size: [e.g., 8, 16, 32]
- Epochs: [e.g., 50-200]
- Optimizer: [e.g., SGD, Adam, AdamW]
- Loss Function: [e.g., CrossEntropy, MSE, Dice Loss, Focal Loss]
```

### 3. Time Series Forecasting Model

```
Build a time series forecasting model for [SPECIFIC DOMAIN] using advanced ML techniques.

**Forecasting Task:** [e.g., Sales Prediction, Stock Price Prediction, Weather Forecasting, Energy Consumption]

**Model Architecture:**
- Model Type: [e.g., LSTM, GRU, Transformer, Prophet, ARIMA, XGBoost]
- Sequence Length: [e.g., 30 days, 12 months, Variable]
- Prediction Horizon: [e.g., Next day, Next week, Next month]

**Time Series Processing:**
- Frequency: [e.g., Daily, Hourly, Monthly, Irregular]
- Seasonality: [e.g., Daily, Weekly, Monthly, Yearly]
- Trend Analysis: [Yes/No]
- Stationarity: [Required/Optional]

**Feature Engineering:**
- Lag Features: [e.g., Previous 7, 14, 30 periods]
- Rolling Statistics: [e.g., Mean, Std, Min, Max]
- Seasonal Features: [e.g., Day of week, Month, Quarter]
- External Features: [e.g., Holidays, Events, Weather]
```

### 4. Recommendation System Model

```
Create a recommendation system for [SPECIFIC PLATFORM] using collaborative and content-based filtering.

**Recommendation Type:** [e.g., User-Item, Item-Item, Content-Based, Hybrid]

**Model Architecture:**
- Algorithm: [e.g., Matrix Factorization, Neural Collaborative Filtering, BERT4Rec, LightGCN]
- Embedding Dimensions: [e.g., 64, 128, 256]
- Loss Function: [e.g., BPR Loss, Hinge Loss, Cross Entropy]

**Data Structure:**
- User-Item Matrix: [e.g., Explicit ratings, Implicit feedback]
- User Features: [e.g., Demographics, Behavior patterns]
- Item Features: [e.g., Categories, Tags, Descriptions]
- Interaction Types: [e.g., Click, Purchase, View, Like]

**Evaluation Metrics:**
- Ranking Metrics: [e.g., NDCG, MAP, MRR]
- Coverage Metrics: [e.g., Catalog Coverage, User Coverage]
- Diversity Metrics: [e.g., Intra-List Diversity]
```

---

## Implementation Guidelines

### Code Structure Template

```python
# 1. Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# 2. Data Preprocessing
class DataPreprocessor:
    def __init__(self):
        pass
    
    def load_data(self):
        """Load and prepare the dataset"""
        pass
    
    def preprocess(self):
        """Apply preprocessing steps"""
        pass
    
    def split_data(self):
        """Split into train/validation/test sets"""
        pass

# 3. Model Architecture
class ModelArchitecture(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ModelArchitecture, self).__init__()
        # Define layers
        
    def forward(self, x):
        # Define forward pass
        pass

# 4. Training Pipeline
class Trainer:
    def __init__(self, model, criterion, optimizer):
        self.model = model
        self.criterion = criterion
        self.optimizer = optimizer
    
    def train_epoch(self, dataloader):
        """Train for one epoch"""
        pass
    
    def validate(self, dataloader):
        """Validate the model"""
        pass
    
    def train(self, train_loader, val_loader, epochs):
        """Complete training loop"""
        pass

# 5. Evaluation
class Evaluator:
    def __init__(self, model):
        self.model = model
    
    def evaluate(self, test_loader):
        """Evaluate model performance"""
        pass
    
    def generate_report(self):
        """Generate performance report"""
        pass

# 6. Inference
class Predictor:
    def __init__(self, model_path):
        self.model = self.load_model(model_path)
    
    def predict(self, input_data):
        """Make predictions"""
        pass
    
    def batch_predict(self, input_batch):
        """Batch prediction"""
        pass

# 7. Main Execution
def main():
    # Initialize components
    preprocessor = DataPreprocessor()
    model = ModelArchitecture()
    trainer = Trainer(model, criterion, optimizer)
    evaluator = Evaluator(model)
    
    # Execute pipeline
    train_loader, val_loader, test_loader = preprocessor.prepare_data()
    trainer.train(train_loader, val_loader, epochs=100)
    evaluator.evaluate(test_loader)
    
if __name__ == "__main__":
    main()
```

---

## Best Practices and Considerations

### 1. Data Quality
- Implement comprehensive data validation
- Handle missing values appropriately
- Address class imbalance if present
- Ensure data privacy and security

### 2. Model Performance
- Use appropriate evaluation metrics
- Implement cross-validation
- Monitor for overfitting
- Regularize when necessary

### 3. Scalability
- Design for production deployment
- Implement efficient data pipelines
- Consider model compression techniques
- Plan for model versioning

### 4. Monitoring and Maintenance
- Implement logging and tracking
- Set up model performance monitoring
- Plan for model retraining
- Document model behavior

### 5. Ethical AI
- Test for bias and fairness
- Ensure transparency
- Implement explainability features
- Consider privacy implications

---

## Usage Instructions

1. **Select the appropriate prompt template** based on your model type
2. **Fill in the bracketed parameters** with your specific requirements
3. **Customize the prompt** for your particular use case
4. **Use the code structure template** as a starting point
5. **Implement the complete pipeline** following best practices
6. **Test thoroughly** before deployment
7. **Document everything** for future maintenance

This prompt framework ensures comprehensive model development while maintaining flexibility for different applications and requirements. 