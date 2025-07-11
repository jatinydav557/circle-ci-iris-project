🔗 👉 **[Watch the Demo on YouTube](https://www.youtube.com/watch?v=4HJRj0dsnsk&list=PLe-YIIlt-fbOSpBoaPA6TyB3S25WSf5sL&index=3&ab_channel=Jatin)**

```markdown
# 🌸 Iris Species Classification: An End-to-End MLOps Pipeline

**Deploying an Iris Classifier on GKE via CircleCI for Continuous Delivery**

This project demonstrates a complete MLOps pipeline for classifying Iris flower species (Setosa, Versicolor, Virginica) based on their sepal and petal measurements. It showcases a modular, object-oriented codebase, automated CI/CD with CircleCI, and scalable deployment to Google Kubernetes Engine (GKE).

---

## 🎯 Project Overview

The Iris flower dataset is a classic and foundational dataset in machine learning, often used for classification tasks. This project utilizes it to build a robust classification model, but more importantly, it focuses on the MLOps engineering aspects: creating an automated, repeatable, and deployable machine learning solution. The goal is to provide a real-time inference service for Iris species classification, ensuring efficient deployment and management in a production environment.

**Key Objectives:**
* **Develop an accurate classification model:** Precisely identify Iris species (Setosa, Versicolor, Virginica).
* **Implement a comprehensive MLOps pipeline:** Automate data processing, model training, and deployment processes.
* **Ensure modularity and reusability:** Design the codebase with OOP principles and clear separation of concerns.
* **Achieve continuous delivery:** Automate the build, test, and deployment process using CircleCI.
* **Ensure scalability and reliability:** Deploy the model as a microservice on Google Kubernetes Engine (GKE).
* **Secure operations:** Manage sensitive credentials and permissions for cloud resources effectively.

---

## ✨ Key MLOps Features & Practices

This project incorporates a wide array of MLOps principles and tools:

* **⚙️ Modular & Object-Oriented Design (`src` directory):**
    * **`components` Module:** Contains distinct classes for each step of the ML pipeline (e.g., `data_processing`, `model_training`).
    * **Data Processing Component:** Includes functionalities for loading raw data, handling outliers (e.g., on 'SepalWidthCm'), and splitting data into training and testing sets.
    * **Model Training Component:** Manages loading processed data, training the Decision Tree Classifier, saving the model, and evaluating its performance with metrics and a confusion matrix.
    * **`logger` & `custom_exception`:** Implements robust logging and custom exception handling for better debugging and monitoring.
* **🧪 Model Training with Decision Tree Classifier:** Utilizes a Decision Tree Classifier (`sklearn.tree.DecisionTreeClassifier`) for its interpretability and effectiveness in classification tasks.
* **📊 Model Evaluation:** Calculates and logs key metrics such as accuracy, precision, recall, and F1-score. Generates and saves a confusion matrix for visual evaluation.
* **🚀 Automated CI/CD with CircleCI:**
    * **CircleCI:** Orchestrates the Continuous Deployment (CD) pipeline, triggered by code changes.
    * Automates steps for code checkout, Docker image building, pushing to Google Artifact Registry, and deploying to GKE.
* **🐳 Docker Containerization:** The Flask web application, serving the inference API, is containerized using Docker, ensuring consistent execution across different environments.
* **📦 Google Artifact Registry:** Docker images are built and pushed to Google Artifact Registry for secure, versioned storage and seamless integration with GCP deployment services.
* **🌐 Google Kubernetes Engine (GKE) Deployment:** The containerized application is deployed to GKE for scalable, highly available, and resilient model serving.
    * **Kubernetes Deployment (`Deployment` resource):** Ensures multiple replicas of the application pod are running for high availability.
    * **Kubernetes Service (`Service` resource of type `LoadBalancer`):** Exposes the application to external traffic, managing load balancing across the pods.
* **🔒 Secure Credential Management:** Implemented secure handling of GCP service account keys within CircleCI, providing fine-grained permissions for accessing Google Cloud resources (`gcloud auth activate-service-account`).
* **☁️ Google Cloud Platform (GCP) Integration:** Leverages GCP services like GKE and Artifact Registry for cloud-native MLOps.

---

## 🏗️ Architecture

The project's architecture is designed for automation, scalability, and reliability:

**Data Flow & Components:**
1.  **Data Source:** Iris dataset (likely `data.csv` in `artifacts/raw/`).
2.  **Code Repository:** The entire codebase is hosted on GitHub.
3.  **CI/CD Trigger:** Any push to the main branch on GitHub triggers the CircleCI pipeline.
4.  **CircleCI Pipeline:**
    * Pulls the latest code from GitHub.
    * Authenticates with Google Cloud using a securely stored service account key.
    * Builds the Docker image for the Flask inference application.
    * Pushes the Docker image to Google Artifact Registry (e.g., `us-central1-docker.pkg.dev/sigma-scheduler-461007-u2/circle-ci-project/circle-ci-project:latest`).
    * Configures `kubectl` to interact with the target GKE cluster.
    * Deploys the application to GKE using the `kubernetes-deployment.yaml` manifest.
5.  **Inference Service:** The deployed Flask application on GKE (managed by Kubernetes Deployment and exposed by a LoadBalancer Service) serves real-time Iris species predictions via a simple web UI.
6.  **Security:** GCP Service Accounts and securely managed credentials handle access and permissions throughout the pipeline and deployment.

*(Consider adding a visual architecture diagram here for better understanding, e.g., a simple block diagram showing the flow from GitHub -> CircleCI -> GCP Artifact Registry -> GKE)*

---

## 📂 Project Structure



.
├── src/
│   ├── **init**.py
│   ├── components/
│   │   ├── **init**.py
│   │   ├── data\_processing.py       \# Loads, handles outliers, splits data
│   │   └── model\_training.py        \# Trains, evaluates, saves model
│   ├── config/
│   │   ├── **init**.py
│   │   └── configuration.py          \# Centralized configuration management
│   ├── constant/
│   │   ├── **init**.py
│   │   ├── application.py
│   │   └── training\_pipeline.py
│   ├── entity/
│   │   ├── **init**.py
│   │   ├── artifact\_entity.py
│   │   └── config\_entity.py
│   ├── exception/
│   │   ├── **init**.py
│   │   └── exception.py              \# Custom exception handling
│   ├── logging/
│   │   ├── **init**.py
│   │   └── logger.py                 \# Detailed logging setup
│   ├── pipeline/
│   │   ├── **init**.py
│   │   └── training\_pipeline.py      \# Orchestrates ML pipeline stages (e.g., data\_processing -\> model\_training)
│   ├── utils/
│   │   ├── **init**.py
│   │   ├── main\_utils.py
│   │   └── ml\_utils.py
│   └── main.py                       \# Main entry for local pipeline execution/orchestration
├── artifacts/                       \# Stores raw data, processed data, and trained models
│   ├── raw/
│   │   └── data.csv                 \# Raw Iris dataset
│   ├── processed/
│   │   ├── X\_train.pkl
│   │   ├── X\_test.pkl
│   │   ├── y\_train.pkl
│   │   └── y\_test.pkl
│   └── models/
│       ├── model.pkl                \# Trained Decision Tree model
│       └── confusion\_matrix.png     \# Confusion matrix visualization
├── .circleci/                       \# CircleCI configuration directory
│   └── config.yml                   \# CircleCI pipeline definition
├── kubernetes-deployment.yaml       \# Kubernetes Deployment and Service manifests for GKE
├── templates/                       \# HTML templates for the Flask web UI
│   └── index.html
├── app.py                           \# Flask application entry point for inference
├── Dockerfile                       \# Docker build instructions for the Flask app
├── requirements.txt                 \# Python dependencies
├── setup.py                         \# Packaging setup
└── README.md                        \# This README file


*Note: `main.py` in `src/` orchestrates the ML pipeline components (data processing and model training), while `app.py` is the entry point for the Flask inference service deployed on GKE.*

---

## 🛠️ Technologies Used

| Category            | Tool/Framework                   | Purpose                                        |
| :------------------ | :------------------------------- | :--------------------------------------------- |
| **Programming** | Python 3.9+                      | Core language                                  |
| **ML Framework** | Scikit-learn                     | Model training (Decision Tree Classifier)      |
| **MLOps Tools** | Docker                           | Containerization for consistency               |
|                     | CircleCI                         | Continuous Delivery orchestration              |
|                     | Kubernetes                       | Container orchestration, deployment on GKE     |
| **Cloud Platform** | Google Cloud Platform (GCP)      | Cloud infrastructure and services              |
|                     | Google Kubernetes Engine (GKE)   | Scalable, resilient model deployment           |
|                     | Google Artifact Registry         | Docker image storage and versioning            |
|                     | GCP Service Accounts             | Authentication & Authorization for cloud resources |
| **Web Framework** | Flask                            | Lightweight API for inference                  |
|                     | Gunicorn                         | WSGI HTTP Server for Flask (for production)    |
| **Data Handling** | Pandas, NumPy                    | Data manipulation and numerical operations     |
| **Visualization** | Matplotlib, Seaborn              | Confusion Matrix plotting                      |
| **Version Control** | Git, GitHub                      | Code versioning and collaboration              |

---

## 🚧 Challenges & Solutions

Developing this end-to-end MLOps pipeline presented several interesting challenges, which were successfully overcome:

* **Data Quality & Outlier Handling:** Ensuring the quality of the Iris dataset, especially handling potential outliers.
    * **Solution:** Implemented `handle_outliers` method in `DataProcessing` to manage outliers using IQR method for specified columns (e.g., `SepalWidthCm`).
* **Model Selection & Evaluation:** Choosing an appropriate classification model and comprehensively evaluating its performance.
    * **Solution:** Employed a Decision Tree Classifier and thoroughly evaluated it using accuracy, precision, recall, F1-score, and a visual confusion matrix, which is saved as an artifact.
* **Kubernetes Deployment & Service Exposure:** Correctly configuring Kubernetes deployments for multiple replicas and exposing the Flask application externally.
    * **Solution:** Defined `Deployment` and `Service` (type `LoadBalancer`) objects in `kubernetes-deployment.yaml` to ensure high availability and external accessibility.
* **CircleCI & GCP Integration for Deployment:** Setting up CircleCI to securely authenticate with GCP and push images to Artifact Registry, then deploy to GKE.
    * **Solution:** Configured `config.yml` to use `google/cloud-sdk:latest` executor, decode `GCLOUD_SERVICE_KEY`, authenticate with `gcloud auth activate-service-account`, and use `gcloud container clusters get-credentials` and `kubectl apply` for deployment.
* **Environment Consistency:** Ensuring the application behaves consistently from local development to Docker containers and GKE.
    * **Solution:** Docker containerization packages the application and its dependencies, guaranteeing consistent execution across all environments.
* **Small Typos - But with exception handling and a bit of chatgpt i overcame the errors and debugged the application.**

---

## 🔮 Future Enhancements

* **MLflow Integration:** Incorporate MLflow for more comprehensive experiment tracking, model versioning, and a centralized model registry.
* **Automated Retraining:** Implement automated retraining triggers based on data drift or model performance degradation in production.
* **More Sophisticated Models:** Experiment with other classification algorithms (e.g., SVM, Random Forest, Neural Networks) and hyperparameter tuning using tools like Optuna or Keras Tuner.
* **Monitoring & Alerting:** Integrate with GCP's Operations Suite (Cloud Monitoring, Cloud Logging, Cloud Trace) for advanced monitoring, alerting, and debugging of the deployed service.
* **Cost Optimization:** Implement horizontal pod autoscaling (HPA) in GKE to automatically scale the number of pods based on CPU utilization or custom metrics, optimizing resource usage.
* **User Authentication:** Add authentication and authorization layers to the Flask API for secure access.

---

## 🤝 Credits

* [Jatin Yadav]
* [Scikit-learn](https://scikit-learn.org/stable/)
* [Flask](https://flask.palletsprojects.com/)
* [Docker](https://www.docker.com/)
* [CircleCI](https://circleci.com/)
* [Kubernetes](https://kubernetes.io/)
* [Google Cloud Platform](https://cloud.google.com/)
* [Gunicorn](https://gunicorn.org/) (if explicitly used in Dockerfile)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)

---

Made with ❤️ by an AI enthusiast who transforms ML, NLP, DL, GenAI, and MLOps concepts into practical, impactful solutions.
```
## 🙋‍♂️ Let's Connect

* **💼 LinkedIn:** [www.linkedin.com/in/jatin557](https://www.linkedin.com/in/jatin557)
* **📦 GitHub:** [https://github.com/jatinydav557](https://github.com/jatinydav557)
* **📬 Email:** [jatinydav557@gmail.com](mailto:jatinydav557@gmail.com)
* **📱 Contact:** [+91-7340386035](tel:+917340386035)
* **🎥 YouTube:** [Checkout the working projects](https://www.youtube.com/@jatinML/playlists)

