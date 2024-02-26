# imageProcessing_STOP
## Proje Açıklaması:
Bu proje, trafik işaretlerinin varlığını tespit etmek için bir görüntü işleme ve makine öğrenimi yaklaşımı kullanmaktadır. İlk adımda, veri kümesi, stop işaretlerini içeren ve içermeyen iki sınıfa ayrılmıştır. Ardından, OpenCV kullanılarak görüntüler gri ölçekte okunmuş, yeniden boyutlandırılmış ve ön işleme adımları gerçekleştirilmiştir. Daha sonra, veri kümesi, eğitim ve test setlerine ayrılmış ve bir CNN modeli oluşturulmuştur. Model eğitimi binary cross-entropy kaybı ve Adam optimizer ile gerçekleştirilmiştir. Son olarak, eğitilen model, bir test görüntüsü üzerinde uygulanarak trafik işareti varlığını tespit etmektedir.

## Kullanılan Teknolojiler:
**Python ve OpenCV:** Proje, görüntü işleme işlemlerini gerçekleştirmek için Python programlama dilini ve OpenCV (Open Source Computer Vision Library) kütüphanesini kullanmaktadır.

**NumPy:** Projede, görüntü verilerini işlemek ve yönetmek için NumPy kullanılmıştır.

**Keras ve TensorFlow:** Yapay sinir ağı modelinin oluşturulması ve eğitimi için Keras kütüphanesi kullanılmıştır. 

**Scikit-learn:** Proje, veri kümesini eğitim ve test setlerine bölmek için Scikit-learn kütüphanesini kullanmaktadır.

# Kullanılan Makine Öğrenimi Algoritmaları:
**Evrişimli Sinir Ağı (Convolutional Neural Network - CNN):**  Projede trafik işaretlerini tanımak için bir CNN kullanmaktadır. 

**Binary Cross-Entropy Loss ve Adam Optimizer:** Modelin eğitimi için binary cross-entropy kaybı (binary_crossentropy) kullanılmıştır.Ayrıca, eğitim sırasında modelin parametrelerini güncellemek için Adam optimizasyon algoritması (optimizer='adam') kullanılmıştır.

# Proje Amacı:
"IBM AI Engineering Profesyonel Sertifikası" kapsamında aldığım Coursera'daki "Introduction to Computer Vision and Image Processing" kursu için geliştirilmiş olan final projesi olarak sunulmuştur.
