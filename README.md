# Pusula_Alparslan_Bugra_Selvi

#### Ad: Alparslan Buğra
#### Soyad: Selvi
#### E-posta: alparslan.bugra@hotmail.com

## Proje Özeti

Bu proje, Pusula Talent Academy Data Science Intern Case Study için hazırlanmıştır. Proje kapsamında, fiziksel tıp ve rehabilitasyon hastalarına ait 2235 gözlem ve 13 özellik içeren bir veri seti kullanılmıştır. Ana hedef, bu ham veriyi temizleyerek, tutarsızlıkları ve eksik değerleri gidererek ve kategorik değişkenleri düzenleyerek potansiyel bir makine öğrenmesi modellemesine hazır hale getirmektir.

Bu çalışma, veri setinin yapısını anlamak için detaylı bir Keşifçi Veri Analizi (EDA) aşamasını ve veriyi modellemeye uygun formata dönüştüren kapsamlı bir ön işleme aşamasını içermektedir.

## Kodu Çalıştırma Talimatları

Bu projeyi yerel ortamınızda veya Google Colab'de çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  **Gerekli Kütüphaneler:** Proje, Python'da `pandas`, `numpy`, `matplotlib`, `seaborn` ve Excel dosyalarını okumak için `openpyxl` kütüphanelerini kullanır. Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:
    ```bash
    pip install pandas numpy matplotlib seaborn openpyxl
    ```
2.  **Veri Seti:** `Talent_Academy_Case_DT_2025.xlsx` adlı Excel dosyasını projenin çalıştığı dizine yerleştirin.
3.  **Kodu Çalıştırma:** Proje kodunu içeren Python dosyasını (`.py`) veya Jupyter Notebook'u (`.ipynb`) çalıştırın. Kod, veriyi otomatik olarak yükleyecek, temizleyecek ve görselleştirmeleri oluşturacaktır.

## Proje Dosyaları

* `Talent.ipynb` ve `TalentPipeline.py`: Projenin tüm veri ön işleme ve EDA adımlarını içeren ana kod dosyası ve düzenlenmiş pipeline seviye kod.
* `Pusula_Alparslan_Bugra_Selvi_Dokuman`: Projenin bulgularını ve uygulanan adımları özetleyen detaylı dokümantasyon dosyası.
* `cleaned_rehabilitation_data.csv`: Tüm ön işleme adımları uygulandıktan sonra elde edilen, modellemeye hazır temizlenmiş veri seti.
* `numerical_distributions.png`: Sayısal değişkenlerin dağılımını gösteren histogram grafiği:
* <img width="1800" height="600" alt="numerical_distributions" src="https://github.com/user-attachments/assets/5fcd6839-0adb-476b-93f4-0cc1063e920b" />
* `categorical_relationships.png`: Kategorik değişkenlerin hedef değişkenle ilişkisini gösteren kutu grafikleri:
* <img width="1800" height="600" alt="categorical_relationships" src="https://github.com/user-attachments/assets/234832f9-ac0d-4eab-8a7c-410309fc281b" />
