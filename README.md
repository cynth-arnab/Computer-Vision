Group research and case studies for Computer Vision Module

# Computer-Vision Case Studies

1)2D Planar Transformations Simulator
The simulator allows users to perform and visualize various 2D transformations such as Translation, Euclidean, Similarity, Affine, and Projective on different geometries including points, lines, and polygons.

2)2D Object Recognition
The DETR (DEtection TRansformer) framework marks a notable advancement in object detection by reimagining the task as a direct set prediction problem, removing reliance on traditional, manually-designed components. This innovative approach streamlines the detection process using a Transformer-based design. In essence, DETR introduces a streamlined and versatile method for object detection, demonstrating the potential for Transformer-based architectures to replace traditional techniques in computer vision tasks.

3)3D Object Reconstruction(Pixel-2-Mesh)
This case study examines recent advancements in 3D reconstruction techniques, emphasizing the role of deep learning and data-driven methods in creating precise 3D models from various input types, such as single images and multi-view data. The study covers various approaches, including shape-from-shading, photometric stereo, and machine learning-based methods, highlighting their progress in addressing the challenges associated with 3D model creation. The use of extensive datasets like ShapeNet plays a critical role in training and evaluating 3D reconstruction algorithms, helping to enhance the accuracy and detail of generated models. As the field continues to develop, the combination of sophisticated neural networks, detailed data annotations, and computational techniques is expected to expand the capabilities of 3D modeling across a wide range of applications, including computer vision, graphics, medical imaging, and virtual reality.

# Computer Vision Research

Image Restoration using SwinIR

The research paper explores the field of image super-resolution (SR), a branch of computer vision
dedicated to enhance low-resolution images into their high-resolution versions. SR technology has
applications in diverse fields like medical imaging, satellite imagery, and security, where high
quality images are essential for accurate interpretation.

Traditional Super Resolution (SR) models, especially those which are based on convolutional neural networks (CNNs), have made substantial progress, but they were found to struggle in capturing long-range dependencies due to their limited focus on local features.

Previous models like SRCNN and SRGAN brought advancements in deep learning for SR, but their performance is often limited in reproducing finer details and maintaining consistent textures across the entire image. Due to these limitations the SR approaches struggle to understand the overall structure of the image that could benefit from incorporating global context alongside local feature extraction. To address these limitations, the authors of SwinIR developed a model build upon the Swin Transformer, a novel transformer architecture that introduces hierarchical self-attention within non-overlapping local windows. This design enables SwinIR to manage a balance between local detail extraction and global feature consistency, overcoming the CNN’s limited contextual understanding.

