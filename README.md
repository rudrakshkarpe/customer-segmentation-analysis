# Customer Segmentation Analysis

📊 This project uses machine learning techniques to perform customer segmentation prediction based on [Kaggle sales data](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/rudrakshkarpe/customer-segmentation-analysis.git
    ```

2. Navigate to the project directory:
    ```bash
    cd customer-segmentation-analysis
    ```

3. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application 

To run the application using Streamlit, make sure you have installed the dependencies as mentioned above. Then, execute the following command:

```bash
streamlit run setup.py
```
## Running using Docker 


```bash
docker build -t customer-segmentation .
```

```bash
docker run -p 8501:8501 customer-segmentation
```

### Note:

**You can find streamlit application running on 127.0.0.1:8501 or localhost:8501. Ignore streamlit URL shown on Docker run**