# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# %%
df = pd.read_csv("dataset_buys _comp.csv")
df.head()

# Tahap 2 : Pra-pemrosesan Data 
# Label Encoding
# %%
le = LabelEncoder()
for col in df.columns[:-1]:  
    df[col] = le.fit_transform(df[col])

print("Dataset Setelah Label Encoding:")
print(df.head())

# Memisahkan Fitur dan Target
# %%
X = df.drop("Buys_Computer", axis=1)
y = df["Buys_Computer"]

print("Fitur (X):")
print(X.head())

print("Target (y):")
print(y.head())


# Tahap 3 : Membagi Data (Training 80% dan Testing 20%)

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Jumlah Data:")
print("Training:", X_train.shape)
print("Testing :", X_test.shape)

# Tahap 4 : Pembuatan dan Pelatihan Model

# %%
model = GaussianNB()
model.fit(X_train, y_train)


# Tahap 5 : Prediksi Data Testing

# %%
y_pred = model.predict(X_test)
y_pred


# Tahap 6 : Evaluasi Model

# %%
print("Akurasi Model:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# %%
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Tidak Layak', 'Layak'],
            yticklabels=['Tidak Layak', 'Layak'])
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.title('Confusion Matrix')
plt.show()