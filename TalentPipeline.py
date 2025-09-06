import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gerekli kütüphanenin yüklendiğinden emin olun.
# !pip install openpyxl

def load_data(file_path):
    """
    Belirtilen yoldaki Excel dosyasını yükler ve bir DataFrame döndürür.
    Dosya bulunamazsa veya okuma hatası olursa None döndürür.
    """
    try:
        df = pd.read_excel(file_path)
        print("Veri dosyası başarıyla yüklendi.")
        return df
    except FileNotFoundError:
        print(f"Hata: {file_path} dosyası bulunamadı.")
        return None
    except Exception as e:
        print(f"Veri yüklenirken bir hata oluştu: {e}")
        return None

def preprocess_data(df):
    """
    Ham veri setini temizler ve modelleme için hazırlar.
    - Metin içeren sayısal sütunları temizler.
    - Eksik değerleri 'Bilinmiyor' olarak doldurur.
    - Virgülle ayrılmış değerleri one-hot encoding ile yeni sütunlara ayırır.
    - Sütun adlarını düzenler.
    """
    if df is None:
        return None

    # Numerik sütunları temizleme ve int'e dönüştürme
    df['TedaviSuresi'] = df['TedaviSuresi'].str.replace(' Seans', '').astype(np.int64)
    df['UygulamaSuresi'] = df['UygulamaSuresi'].str.replace(' Dakika', '').astype(np.int64)
    print("TedaviSuresi ve UygulamaSuresi sütunları temizlendi.")

    # Belirli sütunlardaki eksik değerleri doldurma
    columns_to_fill = ['Cinsiyet', 'KanGrubu', 'KronikHastalik', 'Bolum', 'Alerji', 'Tanilar', 'UygulamaYerleri']
    df[columns_to_fill] = df[columns_to_fill].fillna('Bilinmiyor')
    print("Eksik değerler 'Bilinmiyor' etiketiyle dolduruldu.")

    # Çoklu değer içeren sütunları one-hot encode etme
    multi_value_cols = ['KronikHastalik', 'Alerji', 'Tanilar', 'UygulamaYerleri']
    for col in multi_value_cols:
        # get_dummies fonksiyonu ile yeni sütunlar oluşturma
        dummies = df[col].str.get_dummies(sep=',').add_prefix(f'{col}_')
        df = pd.concat([df, dummies], axis=1)
        # Orijinal sütunu kaldırma
        df = df.drop(col, axis=1)
    print("Çoklu değer içeren sütunlar başarıyla işlendi ve one-hot encode edildi.")

    # Sütun adlarını düzenleme (boşlukları ve özel karakterleri kaldırma)
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('[^A-Za-z0-9_]+', '', regex=True)
    print("Sütun adları düzenlendi.")

    return df

def run_eda(df):
    """
    Veri setini görselleştirerek keşifçi veri analizi (EDA) yapar.
    - Sayısal sütunların dağılımını gösteren histogramlar oluşturur.
    - Kategorik ve hedef değişken arasındaki ilişkiyi gösteren box plot'lar oluşturur.
    """
    if df is None:
        return

    # Sayısal sütunların dağılımını gösteren histogramlar
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    sns.histplot(data=df, x='Yas', kde=True, ax=axes[0])
    axes[0].set_title('Yaş Dağılımı')
    sns.histplot(data=df, x='TedaviSuresi', kde=True, ax=axes[1])
    axes[1].set_title('Tedavi Süresi Dağılımı (Seans)')
    sns.histplot(data=df, x='UygulamaSuresi', kde=True, ax=axes[2])
    axes[2].set_title('Uygulama Süresi Dağılımı (Dakika)')
    plt.tight_layout()
    plt.savefig('numerical_distributions.png')
    print("\nSayısal dağılım histogramları oluşturuldu.")

    # Kategorik sütunların hedef değişkenle ilişkisini gösteren box plot'lar
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    sns.boxplot(x='Cinsiyet', y='TedaviSuresi', data=df, ax=axes[0])
    axes[0].set_title('Cinsiyet ve Tedavi Süresi İlişkisi')
    sns.boxplot(x='KanGrubu', y='TedaviSuresi', data=df, ax=axes[1])
    axes[1].set_title('Kan Grubu ve Tedavi Süresi İlişkisi')
    plt.tight_layout()
    plt.savefig('categorical_relationships.png')
    print("Kategorik ilişkileri gösteren kutu grafikleri oluşturuldu.")

# Ana program akışı
if __name__ == "__main__":
    file_path = 'Talent_Academy_Case_DT_2025.xlsx'
    
    # Veriyi yükle
    raw_data = load_data(file_path)
    
    if raw_data is not None:
        # Veriyi ön işlemeye tabi tut
        cleaned_data = preprocess_data(raw_data)
        
        # Eğer ön işleme başarılıysa
        if cleaned_data is not None:
            print("\n----------------------")
            print("Veri ön işleme tamamlandı. Veri setinin son hali:")
            print(cleaned_data.info())
            
            # Veri görselleştirme ve EDA adımlarını çalıştır
            run_eda(cleaned_data)
            
            # Temizlenmiş veriyi CSV dosyasına kaydet
            cleaned_data.to_csv('cleaned_rehabilitation_data.csv', index=False)
            print("\nTemizlenmiş veri setiniz 'cleaned_rehabilitation_data.csv' olarak kaydedildi.")
            print("Projeniz modellemeye hazırdır.")