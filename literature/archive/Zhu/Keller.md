Skip to Main Content

* [IEEE.org](https://www.ieee.org/)
* [IEEE *Xplore*](https://ieeexplore.ieee.org/Xplore/home.jsp)
* [IEEE SA](https://standards.ieee.org/)
* [IEEE Spectrum](https://spectrum.ieee.org/)
* [More Sites](https://www.ieee.org/sitemap.html)
* * [Donate](https://www.ieee.org/give)
  * [Cart](https://www.ieee.org/cart/public/myCart/page.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore "View Cart")
  * [Create Account](javascript:void()) "Create Account")
  * [Personal Sign In](javascript:void()) "Sign In")

[![IEEE Xplore logo - Link to home](https://ieeexplore.ieee.org/assets/img/xplore_logo_white.svg)](https://ieeexplore.ieee.org/Xplore/home.jsp "Delivering full text access to the world's highest quality technical literature in engineering and technology")

* Browse
* My Settings
* Help

![Hong Kong Baptist University logo](https://ieeexplore.ieee.org/xploreAssets/images/customer_logos//76040_HKBU-Library_Eng-(128x60)_5DE4.gif)

**Access provided by:**Hong Kong Baptist University

[Sign Out](https://ieeexplore.ieee.org/servlet/Login?logout=/document/10657451 "Sign Out")Attention Authors

![IEEE logo - Link to IEEE main site homepage](https://ieeexplore.ieee.org/assets/img/ieee_logo_white.svg)

AllBooksConferencesCoursesJournals & MagazinesStandardsAuthorsCitationsImages (Beta)

[ ]

[ADVANCED SEARCH](https://ieeexplore.ieee.org/search/advanced)

[Conferences](https://ieeexplore.ieee.org/browse/conferences/title/) **>**[2024 IEEE/CVF Conference on C...](https://ieeexplore.ieee.org/xpl/conhome/10654794/proceeding)[](https://ieeexplore.ieee.org/Xplorehelp/ieee-xplore-training/working-with-documents#interactive-html)

# HIT: Estimating Internal Human Implicit Tissues from the Body Surface

**Publisher:** IEEE

Cite This

[PDF](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10657451)

[Marilyn Keller](https://ieeexplore.ieee.org/author/37086447760); [Vaibhav Arora](https://ieeexplore.ieee.org/author/37089428939); [Abdelmouttaleb Dakri](https://ieeexplore.ieee.org/author/589171927736647); [Shivam Chandhok](https://ieeexplore.ieee.org/author/37086834398); [Jürgen Machann](https://ieeexplore.ieee.org/author/728820067309808); [Andreas Fritsche](https://ieeexplore.ieee.org/author/967358943952414)

[All Authors](javascript:void())

4

Cites in

Papers

184

Full

Text Views

* [](javascript:void())
* 
* [](javascript:void())
* [](javascript:void())
* [](javascript:void())

---

[Abstract](https://ieeexplore.ieee.org/document/10657451)

## Document Sections

* [1.Introduction](javascript:void())
* [2.Related Work](javascript:void())
* [3.Human Tissue Data](javascript:void())
* [4.HIT Method](javascript:void())
* [5.Experiments](javascript:void())

Show Full Outline

[Authors](https://ieeexplore.ieee.org/document/10657451/authors)

[Figures](https://ieeexplore.ieee.org/document/10657451/figures)

[References](https://ieeexplore.ieee.org/document/10657451/references)

[Citations](https://ieeexplore.ieee.org/document/10657451/citations)

[Keywords](https://ieeexplore.ieee.org/document/10657451/keywords)

[Metrics](https://ieeexplore.ieee.org/document/10657451/metrics)

[Supplemental Items](https://ieeexplore.ieee.org/document/10657451/media)

## Abstract:

The creation of personalized anatomical digital twins is important in the fields of medicine, computer graphics, sports science, and biomechanics. To observe a subject's anatomy, expensive medical devices (MRI or CT) are required and the creation of the digital model is often time-consuming and involves manual effort. Instead, we leverage the fact that the shape of the body surface is correlated with the internal anatomy; e.g. from surface observations alone, one can predict body composition and skeletal structure. In this work, we go further and learn to infer the 3D location of three important anatomic tissues: subcutaneous adipose tissue (fat), lean tissue (muscles and organs), and long bones. To learn to infer these tissues, we tackle several key challenges. We first create a dataset of human tissues by segmenting full-body MRI scans and registering the SMPL body mesh to the body surface. With this dataset, we train HIT (Human Implicit Tissues), an implicit function that, given a point inside a body, predicts its tissue class. HIT leverages the SMPL body model shape and pose parameters to canonicalize the medical data. Unlike SMPL, which is trained from upright 3D scans, MRI scans are acquired with subjects lying on a table, resulting in significant soft-tissue deformation. Consequently, HIT uses a learned volumetric deformation field that undoes these deformations. Since HIT is parameterized by SMPL, we can repose bodies or change the shape of subjects and the internal structures deform appropriately. We perform extensive experiments to validate HIT's ability to predict a plausible internal structure for novel subjects. The dataset and HIT model are available at https://hit.is.tue.mpg.de to foster future research in this direction.

**Published in: **[2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)](https://ieeexplore.ieee.org/xpl/conhome/10654794/proceeding)

**Date of Conference: **16-22 June 2024

**Date Added to IEEE  *Xplore* : **16 September 2024

**ISBN Information:**

## ISSN Information:

**DOI: **[10.1109/CVPR52733.2024.00334](https://doi.org/10.1109/CVPR52733.2024.00334)

**Publisher:** IEEE

**Conference Location: **Seattle, WA, USA

[![Figure 1. - Left half: From volumetric human MRI scans, we learn to segment human internal tissues: subcutaneous adipose tissue (yellow), intra-muscular and visceral adipose tissue (blue), lean tissue (red), and long bones (white). We segment the MRI to extract a point cloud of the human body surface (red rings) to which we fit a human body model (SMPL, gray mesh). From this internal and external paired data, we learn Human Implicit Tissues (HIT), an implicit volumetric model that predicts the type and location of internal tissue. Right half: input body (blue mesh) and predicted tissues: subcutaneous adipose tissue (yellow) and lean tissue (red). We use OSSO [32] to infer the bones.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-1-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-1-source-large.gif)

 **Figure 1.** Left half: From volumetric human MRI scans, we learn to segment human internal tissues: subcutaneous adipose tissue (yellow), intra-muscular and visceral adipose tissue (blue), lean tissue (red), and long bones (white). We segment the MRI to extract a point cloud of the human body surface (red rings) to which we fit a human body model (SMPL, gray mesh). From this internal and external paired data, we learn Human Implicit Tissues (HIT), an implicit volumetric model that predicts the type and location of internal tissue. Right half: input body (blue mesh) and predicted tissues: subcutaneous adipose tissue (yellow) and lean tissue (red). We use OSSO [[32]](javascript:void()) to infer the bones.

Show All

SECTION 1.

## Introduction

Creating personalized anatomical digital twins of humans is key in fields such as medicine, sports science, biomechanics, and computer graphics. They play an important role in early diagnosis of diseases, performance evaluation, and gait analysis among others. Yet, creating accurate and detailed patient-specific avatars requires expensive medical imaging devices like Magnetic Resonance Imaging (MRI) or Computed Tomography (CT) scanners. Each subject needs to be scanned and the images segmented, often with manual intervention, making the creation of personalized anatomical avatars tedious [[21]](javascript:void()), [[28]](javascript:void()).

In recent years, researchers have shown that the shape of the human body surface is related to the internal body composition [[36]](javascript:void()), [[43]](javascript:void()), [[48]](javascript:void()), [[72]](javascript:void()), leading the way towards fast and non-invasive methods for early screening of body-composition-related pathologies. In addition, recent work shows that predicting internal anatomical structures from the outer surface is also possible [[23]](javascript:void()), [[32]](javascript:void()), [[33]](javascript:void()), paving the way towards the automatic creation of digital twins solely from body surface observations. Body surfaces are now relatively easy to acquire using techniques that fit parametric body models like SMPL [[41]](javascript:void()) to 3D scans or images.

In this work, we focus on three important body tissues: long bones, i.e. femur, tibia, fibula, humerus, ulna, radius, and hips; subcutaneous adipose tissue (SAT), i.e. fat under the skin; and lean tissue (LT), i.e. muscles and organs. From a medical perspective, these tissues are important: an excess of fat with respect to lean tissue is correlated with health risks such as the development of type-II diabetes and cardiovascular disease [[22]](javascript:void()), [[47]](javascript:void()). From a biomechanics perspective, these tissues have different physical properties and dynamic behaviors, i.e. lean tissue is stiffer, adipose tissue is more elastic, whereas bones are rigid. These differences affect, for example, marker-based motion capture (mocap) systems [[40]](javascript:void()), as markers on soft tissue exhibit artifacts [[10]](javascript:void()). Thus, having a good estimate of the tissue distribution could improve mocap accuracy and enable the simulation of soft-tissue compression in the apparel industry. In computer graphics, several methods assume [[65]](javascript:void()) or optimize [[34]](javascript:void()), [[54]](javascript:void()) a *soft tissue layer* attached to a rigid structure to simulate physical interactions of the avatars in a virtual world.

Also, artificial muscle systems [[57]](javascript:void()) are widely used in character animation but these are complex to design by hand. Having a good estimate of the tissue distribution could improve the anatomic realism of these computational models.

To the best of our knowledge, the precise 3D prediction of these layers inside the body,  *given only the outer body surface* , is a novel problem that has not been tackled in the literature.

Specifically, our goal is to provide a prediction of the internal structures within a body model like SMPL for arbitrary body shapes and to be able to repose the predicted tissues. See [Fig. 1]() for a visualization of the resulting 3D representation.

Three main challenges must be overcome to learn a model that predicts the inside of the body from its surface. First, one needs paired observations of the inside and the outside of the body. While medical scanners can capture the raw data, datasets are scarce and usually need to be annotated (segmented). An-other challenge is that scanners that can see inside a body, such as MRI, require the subject to be in a lying down position. This position introduces significant shape deformations due to the dis-placement of the soft tissues through contact with the scanning table. The last challenge is to design a neural network that can be effectively trained to extract the relevant information from the surface of the body to infer the inner tissues. Our approach,  *Human Implicit Tissues (HIT* ), addresses these challenges.

To obtain paired *inside* and *outside* data, we acquired a dataset of full-body MRI scans (260 female and 182 male). We start with a small subset (40 female and 40 male) for which we compute initial segmentations of lean and adipose tissues [[73]](javascript:void()).

We curate them and enrich them with manual segmentations of the long bones and then train a nnUNet [[27]](javascript:void()) to segment all tissues in the full dataset. These segmented volumes provide the distributions of the tissues inside the body.

To represent the outer body surface, we use the SMPL body model [[41]](javascript:void()), which lets us model the dependency of the tissue locations inside the body on the pose and shape of a subject.

But unlike the surface of the body, an explicit mesh is not appropriate to represent the inner tissues, since their topology can significantly vary between subjects. Implicit functions are particularly well suited to model the occupancy in a given volume [[14]](javascript:void()) and recent work has extensively explored their use in modeling the body surface, clothed bodies and clothing itself, but not for modeling internal body structures. In our approach, given a point inside a body, we predict its tissue class; that is, we formulate the problem as a multi-tissue classification problem.

Inspired by recent work on modeling clothed humans and neural rendering [[6]](javascript:void()), [[12]](javascript:void()) we combine implicit and explicit models and learn to map a 3D point inside a SMPL body into a canonical space. This allows us to learn the multi-tissue classification function in the canonical space. The decomposition of the problem into canonicalization and tissue classification offers the advantage of allowing generalization to unseen poses and body shapes. Yet, one more problem remains. Since full-body MRI scans are performed in a prone pose, the bodies exhibit significant deformation which is not modeled by SMPL, as it was learned from upright scans of people. We capture these defor-mations by optimizing the SMPL mesh vertices to tightly fit the body surface extracted from the MRI. These tight fits allow us to quantify the geometric changes between the SMPL model mesh vertices and their deformed version. Our neural network can thus learn the 3D volumetric displacement of internal soft tissue caused by lying down. This allows us to uncompress the surface and internal structures from lying down to an upright position.

In summary, HIT provides a novel representation of the human body that connects the outer surface to the inner structure. It employs a hybrid of implicit and explicit shape representation and effectively extends the SMPL body model to infer internal structures that can be reshaped and reposed. The key contributions of **HIT** are: (a) we formulate the new problem of estimating the 3D structure of human internal tissues from surface observations as a multi-tissue classification problem; (b) we contribute a new dataset, containing the volumetric tissue lo-cation inside the body, extracted from real **MRI** scans, as well as the corresponding SMPL meshes representing the body surface; (c) we learn a volumetric deformation field accounting for the compression between a standing body shape and its counterpart lying prone on an **MRI** table; (d) we propose a neural implicit formulation to represent the tissue locations inside the body and show that this generalizes to new subjects and new poses; (e) we evaluate and ablate the proposed model on the created dataset.

The new dataset and learned models are made available for academic research at [https://hit.is.tue.mpg.de](https://hit.is.tue.mpg.de/).

SECTION 2.

## Related Work

Motivated by prior work on the prediction of body composition from 3D scans [[48]](javascript:void()), [[71]](javascript:void()), [[72]](javascript:void()), silhouettes [[36]](javascript:void()), or images [[43]](javascript:void()), we go further to predict the location of subcutaneous adipose tissue, lean tissue, and the long bones, solely from the external body surface.

### Anatomic Models.

Early models [[20]](javascript:void()), [[66]](javascript:void()) use the Visible Human data [[1]](javascript:void()), consisting of high-quality images from a ca-daver, to build an anatomic model that can be animated. Other works address the creation of detailed personalized anatomic models from data of the hand [[2]](javascript:void()) or the combination of multiple scans of the body [[55]](javascript:void()) into one full-body avatar. Many other personalized anatomic human models have been created, with a focus on physical simulation of the tissues [[26]](javascript:void()), [[29]](javascript:void()), [[57]](javascript:void()), [[68]](javascript:void()), [[76]](javascript:void()), pedagogic purposes [[3]](javascript:void()), [[60]](javascript:void()), or biomechanics [[53]](javascript:void()). The recent statistical model BOSS [[63]](javascript:void()) includes the skeleton and several organs, but, unlike  **HIT** , it does not model lean and adipose tissues.

Several methods create avatars with **soft tissue** deformation, enabling physics simulation. These typically model the soft tissue as a continuum layer coupled to an articulated skeleton [[34]](javascript:void()), [[54]](javascript:void()), [[56]](javascript:void()), [[57]](javascript:void()), [[65]](javascript:void()). This layer can be manually defined [[57]](javascript:void()), es-timated [[56]](javascript:void()), obtained with an actual scan [[54]](javascript:void()), [[65]](javascript:void()), inferred from skin motion observations [[34]](javascript:void()), or estimated using contact sen-sors [[51]](javascript:void()). None of these are validated against clinical data. Some other works have also addressed the modeling of deformation of the hands [[37]](javascript:void()) and feet [[7]](javascript:void()), [[50]](javascript:void()) due to contact with the world.

### Anatomy Inference.

Most internal anatomical structures cannot be inferred from skin observations alone, but some can, such as estimating the skull or jaw from the face shape [[26]](javascript:void()), [[77]](javascript:void()).

Anatomy Transfer [[3]](javascript:void()) deforms an anatomical template model to be consistent with a new body surface. Similarly, Bauer et al. [[5]](javascript:void()) leverage [[3]](javascript:void()) to infer the skeleton inside a body from an **RGBD** image. Guo et al. [[23]](javascript:void()) estimate the deformation of organs as a patient moves, but the organs' initial shapes are obtained by a scan of the patient. Anatomy Completor [[38]](javascript:void()) can complete the shape of missing organs from the shape of the neighboring ones and OSSO [[32]](javascript:void()) can infer the skeletal bones from the skin surface.

Only the last three works [[23]](javascript:void()), [[32]](javascript:void()), [[38]](javascript:void()) evaluate on clinical data.

Recently, SKEL [[33]](javascript:void()) goes further and parameterizes the SMPL body model with a biomechanical skeleton that can be inferred from the body surface.

### Datasets.

Training and evaluation data, i.e. segmented full- body volumetric images, are key for solving this problem. While databases with medical scans [[24]](javascript:void()), [[64]](javascript:void()) exist, their per-pixel au-tomatic segmentation into tissues is not straightforward. To create our paired dataset, we use an **MRI** protocol [[42]](javascript:void()) and an automatic method [[73]](javascript:void()) to obtain initial segmentations, that we manually curate and enrich.

### Human Implicit Shape Models.

Implicit shape represen- tations have a long history and have recently become more popular due to the use of neural networks to learn occupancy or signed distance fields. Here we focus on methods that model deformable volumes like the body surface [[4]](javascript:void()), [[17]](javascript:void()), [[31]](javascript:void()), [[39]](javascript:void()), [[4]](javascript:void()) [[4]](javascript:void()), [[4]](javascript:void())6, [[4]](javascript:void())9,[[58]](javascript:void()), [[70]](javascript:void()), clothed bodies [[6]](javascript:void()), [[11]](javascript:void()), [[12]](javascript:void()), [[19]](javascript:void()), [[25]](javascript:void()), [[52]](javascript:void()), [[58]](javascript:void()), [[6]](javascript:void())7,[[6]](javascript:void())9,[[74]](javascript:void()), and clothing [[16]](javascript:void()), [[59]](javascript:void()). Implicit shape representations enable efficient inside/outside tests, allowing the models to take into account the surrounding scene [[46]](javascript:void()), [[59]](javascript:void()), as well as supporting arbitrary topologies. Implicit functions for representing human bodies mainly use three approaches to encode the input query point: part-based, relative, and global. *Part-based* approaches [[17]](javascript:void()), [[44]](javascript:void()), [[46]](javascript:void()) learn the occupancy in each part's canonical space whereas *relative encoding* approaches encode a point's occu-pancy with respect to joint locations [[75]](javascript:void()), sparse skin vertices [[16]](javascript:void()), or detected keypoints [[45]](javascript:void()). **HIT** uses a *global* approach, which learns occupancy in a canonical pose (namely a “star” pose). SCANimate [[58]](javascript:void()), Meta Avatar [[69]](javascript:void()) and ARAH [[70]](javascript:void()) learn a subject-specific avatar in a canonical space and train a neural network to predict the skinning weights of any point in space.

This learned inverse LBS (Linear Blend Skinning) lets them transform a point to the canonical pose space before querying the occupancy. In gDNA [[12]](javascript:void()), a multi-subject occupancy model is learned in a canonical pose. A root-finding algorithm [[13]](javascript:void()) enables unposing points, and a displacement field that maps shaped points to the canonical space is learned. We leverage a pretrained SMPL occupancy network to generalize to new shapes and poses, and add a new module to model the body compression and pose-dependent deformations.

A few works jointly model two surfaces, e.g. hand object interaction [[30]](javascript:void()) or multiple clothes [[59]](javascript:void()), by adding interpenetration losses. Our multi-tissue classification formulation naturally avoids reasoning about interpenetration.

SECTION 3.

## Human Tissue Data

A crucial requirement for learning the relationship between the body's inner tissues and the body surface is a structured dataset of paired observations. We use **MRI** scans of human subjects that we segment into several tissues. Each pixel of the **MRI** volume is classified as Bone Tissue (BT), Lean Tissue (LT), Intra-Muscular and Visceral Adipose Tissue (IMVAT),

[![Figure 2. - First row: input MRI images. Second row: segmentation results from the nnU-Net. Tissues color-code: bone (white), lean (red), subcuta-neous adipose (yellow), intra-muscular and visceral adipose (blue), empty (black). From left to right: calf, thighs, hips, chest, head and arms, forearms.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-2-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-2-source-large.gif)

 **Figure 2.** First row: input MRI images. Second row: segmentation results from the nnU-Net. Tissues color-code: bone (white), lean (red), subcuta-neous adipose (yellow), intra-muscular and visceral adipose (blue), empty (black). From left to right: calf, thighs, hips, chest, head and arms, forearms.

Show All

Subcutaneous Adipose Tissue (SAT), or Empty (E) (see [Fig. 2]() with segmentation examples). From the segmented volume, we extract the subject's body surface as a point cloud and fit the SMPL [[41]](javascript:void()) body model to it. We also compute tight fits of the SMPL body mesh that capture the flattened body shape extracted from the **MRI** (see [Fig. 3]()). In this way, we create a dataset of paired observations of the inner body tissues together with the human body surface.

### 3.1. MRI Segmentation

#### MRI Scans Dataset.

We work with 442 scans (260 female, 182 male) acquired with a 1.5 T scanner (Magnetom Sonata, Siemens Healthcare) following a standardized protocol for whole body adipose tissue topography mapping [[42]](javascript:void()). All subjects gave prior informed written consent and the study was approved by the local ethics board. Each scan has around 110 slices, slightly varying depending on the height of the subject.

The slice resolution is 256 x 192, with an approximate voxel size of 2 x 2 x 10 mm.

#### Tissue Definitions.

Given an input **MRI** image (slice), our goal is to classify the tissue type of each pixel. For the Bone Tissue (BT) we focus on the long bones: femur, tibia, fibula, humerus, ulna, radius, and hips. We do not segment smaller bones, such as vertebrae, ribs, or phalanges, as, with the limited resolution of the **MRI** images, it is difficult to consistently identify them in the images. The muscles and organs are segmented as Lean Tissue (LT). The Subcutaneous Adipose Tissue (SAT) and the Intra-Muscular and Visceral Adipose Tissue (IMVAT) denote the human fat; SAT is located directly under the skin, whereas IMVAT is located inside the muscles and around the organs. MRI pixels where no tissue is detected are classified as Empty (E). Empty areas include the background outside the body, the lungs, skull cortical bone, and other cavities inside the body.

#### Human Tissue Segmentation.

To segment the whole MRI dataset into tissues, we use a *human-in-the-loop* approach similar to SAM [[35]](javascript:void()). We leverage initial automatic segmentations [[73]](javascript:void()) and manual annotations to train and refine a nnU-Net [[27]](javascript:void()) with the help of human supervision. The full description of the segmentation process is provided in Sup. Mat. 1. In the remainder of the paper, these segmentations are treated as the ground truth internal tissues. To obtain the external shape, we identify the body contour in the segmented images and by using the **MRI** 3D metadata, we extract a *skin* point cloud **s**.

### 3.2. SMPL Fits to the Skin Point Cloud

For each subject **i**, we fit the SMPL body mesh [[41]](javascript:void()) to the *skin* point cloud **S**i. The benefits of doing so are two-fold. First, we obtain the per-subject SMPL mesh **S**i and shape and pose parameters **(**β**i**∈**R**10**,**θ**i**∈**R**69**)**. The pose **θ**i will be used to unpose the **MRI** into a canonical space, and the shape **β**i to model the subject's shape. Second, by allowing the SMPL body mesh to deform and capture the flattened subject's shape in the  **MRI** , we can quantify the displacement field **d**i that the body undergoes when lying in the  **MRI** . This 3D field allows us to effectively model compression.

While SMPL is commonly fitted to a wide variety of data, our situation is unique. SMPL is learned using body scans of people in upright standing poses, thus the learned shape and pose space can not capture the soft-tissue deformation that the body undergoes in the prone position created by lying on the **MRI** table. As a consequence, directly fitting the SMPL body model to the **MRI** point cloud leads to an incorrect subject shape. To solve this problem we propose a two-step fitting approach. First, we compute an initial SMPL tight fit that allows us to compute the volume of the subject. Then, with a volume-preserving constraint, we compute the best SMPL model pose and shape parameters **(**β**i**,**θ**i**)** that match the **MRI** point cloud, obtaining **S**i. We then allow the vertices to deform, resulting in a deformed mesh **F**i that tightly fits the **MRI** surface. The two-step optimization details are provided in Sup. Mat. 2 and [Fig. 3]() illustrates the obtained results.

### 3.3. Human Implicit Tissues (HIT) Dataset

The new HIT dataset contains, for each subject **i**:**a**) the volu-metric image segmented into BT, LT, SAT, IMVAT, and **E**,**b**) the image MRI center and per-pixel spacing, to transform indices from the volumetric image into 3D metric locations, and c) the

[![Figure 3. - SMPL fits to MRI point clouds. The SMPL fit <span class=](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-3-source-small.gif)\mathrm{S}_{i}\mathrm{S}_{i} (left) does not capture the flattened shape, the tight fit $$ (right) does.&#34; /&gt;](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-3-source-large.gif)

 **Figure 3.** SMPL fits to MRI point clouds. The SMPL fit **S**i (left) does not capture the flattened shape, the tight fit **F**i (right) does.

Show All

#### Final Three-Layer Representation.

The Intra-Muscular and Visceral Adipose Tissue (IMVAT) segmented in the MRI images is sparsely located around the muscles and abdominal organs (blue in [Figs. 1]() and [2]()). As its precise 3D location highly varies among people, we leave the precise localization of IMVAT for future work and infer 3 layers of tissue: Bone Tissue (BT), Lean Tissue and Intra-Muscular and Visceral Adipose Tissue (LT + IMVAT) and Subcutaneous Adipose Tissue (SAT), which are used for anatomic digital twins [[34]](javascript:void()), [[54]](javascript:void()), [[56]](javascript:void()), [[65]](javascript:void()). That is, in the remainder of the paper, we merge IMVAT with the surrounding LT structures and refer to them together as LT.

SECTION 4.

## HIT Method

### Problem Statement.

We formalize the inference of the tissues inside the body as a 4-tissue classification problem (BT, LT **(**+ IMVAT), SAT, E). **HIT** learns an implicit function that takes as input SMPL shape and pose parameters **(**β**,** **θ**) and a **3**D point x, and outputs the tissue class at that point.

### 4.1. HIT Spaces

To learn the tissue occupancy, **HIT** warps the data from the input MRI space into a canonical space. These warps are defined between four spaces, illustrated in [Fig. 4](). The *canonical space* is where the SMPL template mesh,  **T** , in a “star” pose, is defined. Points in the canonical space are indexed by **x**c. The *shaped space* is where additive offsets, **d**β**∈**R**N**v**×**3, controlled by the shape **β** of the subject, are applied to the template. We denote points there as **x**β**=**x**c**+**d**β. The shaped points can then be posed through linear blend skinning into the *posed space* **x**p**=** LBS **(**x**β**,**w**,**θ**), where **w**∈**R**N**p** is a vector of blend-weights, **N**p**=**24 is the number of SMPL body parts, and **θ** represents the pose parameters. Finally, to model the MRI table compression on the body, we define volumetric offsets **d**x**c**o**m**p**∈**R**3** and denote points in the *original* **M**R**I** *space* **x**m**=**x**p**+**d**x**c**o**m**p. Note that points in all spaces live in **R**3 and can be inside, outside, or on the SMPL surface. skin point cloud **S**1, the fitted SMPL model mesh **S**c represented by its parameters **(**θ**i**,** **β**i**), as well as the SMPL tight fit **F**2. From b) we compute the compression displacements **d**c**o**m**p**∈**R**N**v**, be-tween the **S**i and **F**i vertices, where **N**v**=**6890 are the number of SMPL vertices. Note that the original MRI images are not included. This dataset is made available for academic research.

[![Figure 4. - HIT defines four <span class=](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-4-source-small.gif)\mathbb{R}^{3}\mathbb{R}^{3} spaces. A point $$ in the original MRI space corresponds to $$ in the posed space, $$ in the shaped space, and $$ in the canonical space.&#34; /&gt;](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-4-source-large.gif)

 **Figure 4.** HIT defines four **R**3 spaces. A point **x**m in the original MRI space corresponds to **x**p in the posed space, **x**β in the shaped space, and **x**c in the canonical space.

Show All

[![Figure 5. - HIT modules <span class=](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-5-source-small.gif)(\mathcal{D},\mathcal{U},S^{\backslash }(\mathcal{D},\mathcal{U},S^{\backslash }, and networks $$ to warp points between spaces.&#34; /&gt;](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-5-source-large.gif)

 **Figure 5.** HIT modules **(**D**,**U**,**S**∖**, and networks **(**C**,**B**,**W**)** to warp points between spaces.

Show All

### 4.2. HIT Architecture

Our architecture is composed of 4 building blocks. Three modules enable warping an MRI point into the canonical space **x**c**=**(**S**∘**U**∘**D**)**(**x**m**,** **β**,** **θ**) by Decompressing **(**D**)**, Unposing **(**U**)** and Deshaping **(**S**)**. The warping architectures are illustrated in [Fig. 5](). Once the warped point is in the canonical space, the network **T**(**x**c**)** predicts its tissue class.

#### Deshaping Module.

Given a shape **β**, the Deshaping module **s** transforms shaped points into canonical points, i.e. **S**(**x**β**,**β**)**=**x**c. In the module, the **function **B predicts the offsets **B**(**x**β**,**β**)**=**d**β, which are subtracted from **x**β to obtain **x**c (see [Fig. 5]() bottom diagram).

#### Unposing Module.

Given shape and pose parameters, the Unposing module **U** warps points from the *posed space* into the *shaped space:* **U**(**x**p**,**β**,**θ**)**=**x**β. Similar to Chen et al. [[12]](javascript:void()), this module uses two MLPs: **B**(**x**β**,**β**)**=**d**β defined in the previous paragraph and the function **W**(**x**c**)**=**w** which predicts the skinning weights w of a point in the canonical space (see [Fig. 5]() middle diagram). Unposing points inside or outside a posed SMPL mesh is challenging because the skinning weights are only defined on the SMPL surface. Chen et al. use a root-finding algorithm [[9]](javascript:void()) that finds candidate points **{**x**β**i**}** for a given posed point **x**p. Then their SMPL occupancy prediction is used to decide on the best candidate. However, this is not applicable in our multi-tissue case; i.e. if a point has two roots, one in LT and one in BT, there is no way to know which one is correct. To overcome this limitation, we initialize the root finding with skinning weights w, fetched from the closest SMPL vertex. This allows the iterative algorithm to converge to the skinning weights that properly unpose the point.

#### Decompression Module.

To model the body deformation displacement induced by the MRI table, we learn a Decompres-sion module **D** that maps points in the MRI space to the posed space: **D**(**x**m**,**β**,**θ**)**=**x**p. We do so by learning to predict the volumetric compression displacements **d**x comr, which generalize the computed **d**c**o**m**p** on the SMPL surface. However, learning the volumetric body decompression is challenging: a **3**D point **x**m can represent a different anatomic region for two different subjects. Thus, instead of learning to predict displacements in the MRI space, we first unpose **x**m into the *shaped space* **x**β and predict **C**(**x**β**,**β**)**=**d**x**c**o**m**p so that **x**m**+**d**x**c**o**m**p**=**x**p (see [Fig. 5]() top diagram). The *shaped space* has a natural shape consistency which helps predict the compression.

#### Multi-Tissue Network.

Once points are in the  *canonical space* , **HIT** uses an MLP to predict the point tissue class **T**(**x**c**)**= { **E**,**L**T, SAT, BT}.

Sup. Mat. 3 provides the network implementation details.

### 4.3. Training, Losses and Sampling

#### Training.

To train **HIT** we proceed in 3 steps. First **B** and **W** are pre-trained by randomly sampling shaped and posed SMPL bodies. In parallel, **C** is pre-trained using the computed **d**c**o**m**p** (**see** Sec. 3). Then, the weights of **C** are frozen, and **B**,**W**,**T** and **A**Λ are jointly trained on the HIT dataset. We note the network's trainable weights as **ψ**∗ and use the subscript **∗** to refer to the network name, i.e. **ψ**B are the weights of the network **B**. To train our architecture we minimize the following losses.

#### Deshaping Loss.

Let **x**β**v** be a vertex of the shaped mesh SMPL **(**β**)**, and **x**c**v** be the corresponding vertex on the SMPL template mesh. To train the weights **ψ**B, we enforce the pre-dicted displacement to match the reversed SMPL's **β** offset at the body surface level by minimizing

**l**s**(**ψ**t**3**)**=**MSE**v**(**B**(**x**β**v**,**β**)**−**(**x**c**v**−**x**β**v**)**)**,**(1)

View Source![Right-click on figure for MathML and additional features.](https://ieeexplore.ieee.org/assets/img/icon.support.gif "Right-click on figure or equation for MathML and additional features.")where **M**S**E**,**1**, is the mean square error over sampled points.

#### Skinning Weight Loss.

To train the **ψ**W weights we enforce the predicted skinning weights to be consistent with the SMPL ones by minimizing

**l**w**(**ψ**W**)**=**MSE**v**(**W**(**x**c**v**)**−**w**v**)**,**(2)

View Source![Right-click on figure for MathML and additional features.](https://ieeexplore.ieee.org/assets/img/icon.support.gif "Right-click on figure or equation for MathML and additional features.")where **w**v**∈**R**N**p denotes the SMPL's skinning weights of the SMPL template vertex **x**c**v**.

#### Decompression Loss.

To train **C** to predict a displacement that is similar to the one between **x**m**v** and **x**p**v**, we minimize

**l**c**(**ψ**C**)**=**MSE**v**(**C**(**U**(**x**m**v**,**β**)**)**,**x**p**v**−**x**m**v**)**(3)**

View Source![Right-click on figure for MathML and additional features.](https://ieeexplore.ieee.org/assets/img/icon.support.gif "Right-click on figure or equation for MathML and additional features.")

#### Multi-Tissue Loss.

Given a point sampled inside compressed body **x**m**k** and canonicalized to **x**c**k**, we train **T** to predict the correct tissue label. This is done by optimizing the weighted cross-entropy loss between the tissue predictions and the training data, where weights are inversely proportional to the tissue sample size.

#### Sampling Strategy.

The MRI scans have a discrete volumetric representation. To avoid aliasing artifacts, we train HIT with points **x**m**k** sampled at the center of voxels. Note that this only holds for querying the GT volume; once the implicit function is learned, one can sample arbitrary locations inside the body and extract smooth tissue volumes.

Uniformly sampling the MRI voxel centers means that the canonical space is not uniformly sampled, e.g. the space between the legs is wider in the canonical space. Thus, we also uniformly sample points outside the SMPL template mesh in the canonical space and classify them as E.

As the MRI resolution is low for hands, we force these parts to be always predicted as LT by uniformly sampling points in the canonical space inside the hands' bounding boxes.

SECTION 5.

## Experiments

To evaluate HIT we split the data into 80% train, 10% validation and 10% test sets (females 201/25/26, males 136/17/16), and we train separate models for males and females as the literature reports significant differences in body composition [[8]](javascript:void()).

**Table 1. **Quantitative evaluation for females and males on the three tissues (LT, SAT, BT). DICE Score (D.S.) - higher is better and Δ % is the relative difference in the quantity prediction in percent - lower is better.

[![Table 1.- Quantitative evaluation for females and males on the three tissues (LT, SAT, BT). DICE Score (D.S.) - higher is better and Δ % is the relative difference in the quantity prediction in percent - lower is better.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-table-1-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-table-1-source-large.gif)

### 5.1. Internal Tissues Evaluation

Since we address a novel problem, to the best of our knowledge, no prior work can be directly used for comparison: e.g. OSSO [[32]](javascript:void()) solely predicts the bone structures. To have a numeric calibration for the multi-tissue problem, we propose a *Chance* baseline, which for each queried point predicts the tissues [E, LT, SAT, BT] with probabilities 0.03, 0.52, 0.41, 0.04 and 0.04, 0.60, 0.32, 0.04 for females and males respectively. These values follow the average percentage of each tissue in the training set.

To quantitatively evaluate the HIT architecture, we report mean Dice scores [[18]](javascript:void()) for each predicted tissue on the test set. Additionally, we compute the relative error of the predicted tissue quantity, by computing **Δ**=**|**V**p**r**e**d**−**V**G**T**|**/**V**J**3**, where **V**p**r**e**d**,**V**G**T**,**V**B**∈**R are the volumes of the predicted tissues, ground-truth tissues, and full body respectively.

Table 1 shows that the HIT Dice scores are significantly better than the Chance baseline. Additionally, [Fig. 6](), [Fig. 7](), and Sup. Mat. 5.2 present qualitative results of the tissue predictions on transverse planes and in 3D. As visible in [Fig. 6]() the predicted inner tissues are consistent across the body and exhibit plausible compression. In addition, most errors arise at the tissue interfaces. The 3D visualization in [Fig. 7]() and Sup. Mat. 5.3 also shows that the obtained 3D meshes are visually consistent with the GT ones. Let us note that extracting per-tissue 3D meshes from a multi-label function is not trivial.

In Sup. Mat. 4 we detail how we do this.

To further put HIT bone predictions in context, we numerically compare to OSSO [[32]](javascript:void()) by measuring the distance between the segmented bones and the predicted ones. We show in Sup. Mat. 5.4 that HIT outperforms OSSO in terms of mean absolute error.

Regarding the metric **Δ** in Tab. 1, measuring the predicted tissue volume, it is interesting to note that HIT is on pair with the Chance baseline (or even under-performs it for female SAT).

The Chance **△** metric is quantifying the error of predicting the mean volume, i.e. the variability in the dataset volumes. The similar HIT **△** metric points out that, in fact HIT is predicting an average tissue quantity. This is not surprising, as HIT predictions are conditioned on 10 SMPL shape parameters, which cannot capture all individual shape details. In Sec. 6 we discuss how future work could improve the current predictions.

[![Figure 6. - Transverse slices (female): (left) GT tissues, (middle) HIT predictions, (right) accuracy (green correct, red otherwise).](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-6-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-6-source-large.gif)

 **Figure 6.** Transverse slices (female): (left) GT tissues, (middle) HIT predictions, (right) accuracy (green correct, red otherwise).

Show All

[![Figure 7. - From left to right: SMPL fit S (gray), HIT LT prediction, GT LT, HIT SAT prediction, GT SAT.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-7-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-7-source-large.gif)

 **Figure 7.** From left to right: SMPL fit S (gray), HIT LT prediction, GT LT, HIT SAT prediction, GT SAT.

Show All

### 5.2. Generalisation to New Body Shapes and Poses

To generalize to new body shapes and poses, correctly modeling the compression is key. We thus ablate the HIT compression module by learning **HIT**n**c**m**p**, a HIT variant without the compression module. As visible in [Fig. 8](), **HIT**n**c**m**p** can not generalize and generates compressed results for standing bodies. See Sup. Mat. 5.1 for a visualization of the HIT learned displacement and compression fields.

[![Figure 8. - Prediction of the SAT occupancy for the mean SMPL body in T-pose. Left: SMPL mesh, middle HIT, right <span class=](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-8-source-small.gif)\text{HIT}_{\mathrm{n}\mathrm{c}\mathrm{m}\mathrm{p}}\text{HIT}_{\mathrm{n}\mathrm{c}\mathrm{m}\mathrm{p}}. Note how the compression remains in the inference for $$. Color code: distance to the SMPL mesh (blue $$ cm, red $$).&#34; /&gt;](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-8-source-large.gif)

 **Figure 8.** Prediction of the SAT occupancy for the mean SMPL body in T-pose. Left: SMPL mesh, middle HIT, right **HIT**n**c**m**p**. Note how the compression remains in the inference for **HIT**n**c**m**p**. Color code: distance to the SMPL mesh (blue **=**0 cm, red **=**5**cm**).

Show All

[![Figure 9. - Prediction of the lean tissues for different body shapes. Varying (left) the first component of SMPL - related to size on females - and (right) the second one - related to weight - for males in the range <span class=](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-9-source-small.gif)\{+2,\ -2\}\{+2,\ -2\}. The predicted tissues consistently adapt to the new shapes, leading to visually plausible predictions.&#34; /&gt;](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/10654794/10654797/10657451/10657451-fig-9-source-large.gif)

 **Figure 9.** Prediction of the lean tissues for different body shapes. Varying (left) the first component of SMPL - related to size on females - and (right) the second one - related to weight - for males in the range **{**+**2**,** **−**2**}. The predicted tissues consistently adapt to the new shapes, leading to visually plausible predictions.

Show All

#### New Shapes.

To explore how the HIT tissue predictions generalize to new body shapes we vary the input SMPL shape components related to height and weight [[41]](javascript:void()), in the range of **[**−**2**,**+**2**]**. [Figure 9]() shows that HIT predicts plausible tissues that vary in accordance with the person's shape.

#### New Poses.

Learning in the SMPL canonical space enables querying skinning weights for each point inside the body, and thus the inferred tissue volumes can be easily reposed. [Figure 1]() shows the reposed tissue volumes for two different poses. Note that at inference time, the compression network is bypassed to yield non-compressed body shapes.

SECTION 6.

## Discussion and Conclusion

HIT introduces the new problem of inferring the human tissues inside of a body from a surface observation only. This work is relevant for medicine, sports science, biomechanics, and computer graphics as it can ease the creation of personalized anatomic digital twins. We formulate the problem as a multi-tissue classification task and learn an implicit function that takes, as input, a query point, and SMPL pose and shape parameters and predicts its tissue class. To learn HIT, we create a dataset of paired full-body volumetric segmented MRI scans and SMPL meshes capturing the body surface shape. We evaluate and ablate the proposed model on the created dataset, showing the quality of the HIT reconstructed tissues.

To the best of our knowledge, this is the first work to predict the volumetric composition of the tissues inside the body from an outer surface observation. We show that it is possible to predict health-relevant tissues inside the body, and most importantly, we give a first quantification of the accuracy of these predictions against medical data. To foster future research on this topic, the dataset and HIT model are made available for academic purposes at [https://hit.is.tue.mpg.de](https://hit.is.tue.mpg.de/).

### Limitations.

While we learn to uncompress the soft tissue from the body surface, we can not validate the behavior of this uncompression inside the body for now. This would require specific data or simulation. Also, the current use of HIT for a precise prediction of the tissue percentage remains limited. Our work does not explore the precise location of Intra-Muscular and Visceral Adipose Tissue (IMVAT). Its structure is very sparse and, while its volume quantification is relevant in medicine, it is not clear whether its exact pixel-wise location is.

Still, the HIT dataset provides the IMVAT segmentation masks, which will enable future exploration.

### Future Work.

The distribution of the lean and subcutaneous adipose tissues inside the body is relatively well structured; i.e. neighbouring points inside the body will, most of the time, be of the same tissue. While these structures naturally emerge in our results, we did not use any explicit loss to enforce the tissue's spatial consistency. One direction to improve the accuracy of the predictions could be to study structural losses, for instance, adversarial networks on slices of the predicted volume, enforcing the structure of multiple points at once.

Moreover, our approach uses a SMPL body mesh for inference and does not include the individual features present in the point cloud of the scan. Future methods could explore how to integrate this information to improve the predictions.

### Risks.

Our work has associated privacy risks. Today, many methods can estimate accurate SMPL bodies from images [[15]](javascript:void()), [[61]](javascript:void()), and HIT can infer their internal tissues. As a good estimate of the body composition relates to health risks [[22]](javascript:void()), [[36]](javascript:void()), [[62]](javascript:void()), HIT could allow the estimation of health risks from a single image of a person. This is valuable as an early diagnostic tool when used with the person's knowledge but could turn into a risk if it is used without consent.

### ACKNOWLEDGMENTS

Marilyn Keller was supported by the International Max Planck Research School for Intelligent Systems. Shivam Chandhok and Sergi Pujades' work was funded by the ANR JCJC SEMBA project. We thank Kate Duquesne and Emmanuel Audenaert for the initial interactive bone segmentations. MJB CoI Discolosure: [https://files.is.tue.mpg.de/black/CoI_CVPR_2024.txt](https://files.is.tue.mpg.de/black/CoI_CVPR_2024.txt)

## Authors

## Figures

## References

## Citations

## Keywords

## Metrics

## Supplemental Items

[](https://ieeexplore.ieee.org/ielx8/10654794/10654797/10657451/mm_530000d480.zip?arnumber=10657451)## Description

Description not available.

Review our [Supplemental Items documentation](https://ieeexplore.ieee.org/Xplorehelp/Help_Multimedia.html) for more information.

<iframe id="google_ads_iframe_/3890430/IEEEXplore/DocDetailsTop_2" name="google_ads_iframe_/3890430/IEEEXplore/DocDetailsTop_2" title="3rd party ad content" width="300" height="250" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" aria-label="Advertisement" tabindex="0" allow="private-state-token-redemption;attribution-reporting" data-google-container-id="1" data-load-complete="true"></iframe>

More Like This

[Three-Dimensional Display from Cross-Sectional Tomographic Images: An Application to Magnetic Resonance Imaging](https://ieeexplore.ieee.org/document/4307813/)

IEEE Transactions on Medical Imaging

Published: 1987

[Fast and Smart Segmentation of Paraspinal Muscles in Magnetic Resonance Imaging with CleverSeg](https://ieeexplore.ieee.org/document/8919679/)

2019 32nd SIBGRAPI Conference on Graphics, Patterns and Images (SIBGRAPI)

Published: 2019

[Show More](javascript:void())

<iframe id="google_ads_iframe_/3890430/IEEEXplore/DocDetailsMiddle_2" name="google_ads_iframe_/3890430/IEEEXplore/DocDetailsMiddle_2" title="3rd party ad content" width="300" height="600" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" aria-label="Advertisement" tabindex="0" allow="private-state-token-redemption;attribution-reporting" data-google-container-id="2" data-load-complete="true"></iframe>

# References

**References is not available for this document.**

## IEEE Personal Account

* [Change username/password](https://www.ieee.org/profile/changeusrpwd/showChangeUsrPwdPage.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)

## Purchase Details

* [Payment Options](https://www.ieee.org/profile/payment/showPaymentHome.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
* [View Purchased Documents](https://ieeexplore.ieee.org/articleSale/purchaseHistory.jsp)

## Profile Information

* [Communications Preferences](https://www.ieee.org/ieee-privacyportal/app/ibp?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
* [Profession and Education](https://www.ieee.org/profile/profedu/getProfEduInformation.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
* [Technical interests](https://www.ieee.org/profile/tips/getTipsInfo.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)

## Need Help?

* [US &amp; Canada: +1 800 678 4333](tel:+1-800-678-4333)
* [Worldwide: +1 732 981 0060](tel:+1-732-981-0060)
* [Contact &amp; Support](https://ieeexplore.ieee.org/xpl/contact)

## Follow

* [](https://www.facebook.com/IEEEXploreDigitalLibrary/ "Follow IEEE Xplore on Facebook, opens in a new tab")
* [](https://www.instagram.com/ieeexplore_org "Follow IEEE Xplore on Instagram, opens in a new tab")
* [](https://www.linkedin.com/showcase/ieee-xplore "Follow IEEE Xplore on LinkedIn, opens in a new tab")
* [](https://www.youtube.com/ieeexplore "Follow IEEE Xplore on Youtube , opens in a new tab")
* [](https://twitter.com/IEEEXplore?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor "Follow IEEE Xplore on Twitter, opens in a new tab")

[About IEEE *Xplore*](https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/about-ieee-xplore) | [Contact Us](https://ieeexplore.ieee.org/xpl/contact) | [Help](https://ieeexplore.ieee.org/Xplorehelp) | [Accessibility](https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/accessibility-statement) | [Terms of Use](https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/terms-of-use) | [Nondiscrimination Policy](http://www.ieee.org/web/aboutus/whatis/policies/p9-26.html) | [IEEE Ethics Reporting](http://www.ieee-ethics-reporting.org/) | [Sitemap](https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/ieee-xplore-sitemap) | [IEEE Privacy Policy](http://www.ieee.org/about/help/security_privacy.html)

A public charity, IEEE is the world's largest technical professional organization dedicated to advancing technology for the benefit of humanity.

© Copyright 2026 IEEE - All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies.

<iframe src="https://ieeexplore.ieee.org/document/" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" data-tags="bottom" title="Usabilla Feedback Button" class="usabilla-live-button" id="usabilla_live_button_container_iframe946411193"></iframe>

[View PDF](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10657451&ref=)
