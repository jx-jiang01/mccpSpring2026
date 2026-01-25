# Image Captioning via Masked
Conditional Diffusion

**Authors**: Jiayi Zhou, Chen Li, Huidong Tang, Sayaka Kamei, Shuai Jiang, Yasuhiko Morimoto

## Abstract

Current image captioning methods mainly adopt the autoregressive framework that operates through a next-token prediction paradigm. A non-autoregressive method called diffusion models has shown superiority in image generation. However, their potential in image captioning remains
underexplored due to the visual-language misalignment. In this work, we present a novel Masked Conditional Diffusion model (MC-Diffusion). It contains a discrete denoising diffusion probabilistic model (D3PM) and a pre-trained vector quantized variational autoencoder (VQ-VAE). Specifically, we first extract discrete image features via
VQ-VAE. Conditioned on these discrete image features, the discrete diffusion model generates captions through transformer blocks to establish discrete-to-discrete alignment. Furthermore, we propose a simple yet effective guidance method, named Masked Condition Strategy (MCS). Compared with classifier-free guidance, our proposed method achieves finer-grained visual-language alignment while demonstrating superior capability in model guidance. Experiments on the CUB-200 dataset show that the proposed method performs better than baselines on several metrics. Compared with classifier-free guidance, MCS achieves similar performance on reference-based metrics (e.g., BLEU, Meteor, etc.) while alleviating the hurt on CLIPScore.

Image Captioning Diffusion Model Vector Quantized Variational Autoencoder.

**Keywords**: Image Captioning Diffusion Model Vector Quantized Variational Autoencoder.

---

## Introduction

Image captioning is a task that uses a neural network to generate relevant text for a given image. Image captioning enables automated textbook illustration explanations, medical imaging report generation (e.g., X-ray descriptions), and real-time assistance for visually impaired individuals. This multimodal task bridges the realms of natural language processing and computer vision. Autoregressive models stand out as a widely used approach to generate captions word-by-word. The up-to-date methods [citation] have achieved remarkable results by capitalizing on this next-token prediction paradigm. However, such techniques suffer from unidirectional semantic passing issue and accumulated prediction error. Specifically, tokens are predicted from left to right. If a wrong word is sampled, this error propagates unidirectionally, amplifying inaccuracies in subsequent tokens.

To alleviate the limitations, researchers have adopted non-autoregressive methods for image captioning
that allow for bidirectional semantic passing. One such approach involves adapting diffusion models [citation], which have succeeded in image generation [citation], to image captioning. With the pioneering work of Bit Diffusion [citation], which explores a continuous diffusion model to generate discrete texts, SCD-Net [citation] can generate captions with
the relevant semantic conditions. DDCap [citation] first utilizes a discrete diffusion model in image captioning.

Despite their success, existing diffusion-based image captioning methods still have some limitations. On one hand, there exists a continuous-to-discrete misalignment. Existing methods [citation] extract the continuous image representation before serving as conditions to generate captions. Images exhibit continuity and high redundancy with low information density, whereas text operates through discrete tokens carrying highly abstract information, enabling concise visual description. It is non-trivial to align continuous image features to discrete
text features well. On the other hand, the coarse-grained image-sentence alignment fails to capture localized semantics. Current works mainly employ either a full conditional model or classifier-free guidance [citation] (some image conditions are removed) to establish visual-language alignment. However, while these approaches achieve alignment to some extent, their coarse-grained image-sentence level alignment renders models incapable of capturing fine-grained semantic correspondences. For instance, they may align the image with the full caption but fail to establish correct object-word correspondences (e.g., linking detected ``dog'' regions to the token ``cat'' in text).

[Figure: Discrete diffusion model for text generation. The noise depends on the transition matrix. [M] refers to the mask token.]

To mitigate the weakness above, we devise a **M**asked **C**onditional **Diffusion** model (MC-Diffusion). We start with a Vector Quantised Variational AutoEncoder (VQ-VAE) [citation] as an image encoder to extract discrete image features. We leverage a discrete diffusion model [citation] for generating captions. Specifically, as shown in Figure [reference], the forward process of the discrete diffusion model corrupts the token sequence into noise through a transition matrix. Starting from noisy data, the reverse process reconstructs the text through iterative denoising. Conditioned on the discrete image features, MC-Diffusion can establish a unified discrete-to-discrete alignment framework that explicitly bridges visual and textual semantics.

The MC-Diffusion can further achieve fine-grained visual-language alignment. Through discrete image features modeled by VQ-VAE, we introduce a simple yet effective guidance method, named Masked Condition Strategy (MCS). For each data sample, a portion of the discrete image features is removed before serving as the condition to generate a caption. Our work leverages the advantage of VQ-VAE in modeling discrete features, enabling masking on high-level image features spanning across multiple regions to establish fine-grained image-caption alignment. In addition, the MCS can be regarded as the fine-grained form of classifier-free guidance, as it involves removing a portion rather than the entire image features for certain examples.

To verify the MC-Diffusion, we conduct image captioning experiments on the CUB-200 dataset [citation]. Our method achieves better results on all reference-based metrics than baselines. We further verify the proposed MCS, experiment results confirm our approach achieves similar performance on reference-based metrics while alleviating the hurt of CLIPScore [citation]. The main contributions of this work are as follows:
- We propose MC-Diffusion, a novel framework combining VQ-VAE and discrete diffusion models to establish discrete-to-discrete alignment.
- We design the MCS to enable fine-grained visual-language alignment through partial image feature masking.
- Experiments demonstrate the superior performance of MC-Diffusion compared with baseline methods, validating its effectiveness in alignment.
itemize

## Related Work

### Autoregressive Models

Early image captioning methods [citation] focus on utilizing a CNN as an image encoder to learn high-level representations, followed by an RNN text decoder to predict the caption word-by-word. Later on, techniques [citation] that leverage the attention mechanism are explored to predict the caption by concentrating on the relevant image region. Inspired by the triumph of Transformer [citation], [M^2] transformer [citation] exploits mesh-like connectivity to learn both low-level and high-level image features. RSTNet [citation] enhances the transformer decoder with the adaptive-attention module to measure the importance of the visual-language prior. Recent advances have focused on exploring large vision-language models which contain billions of trainable parameters, such as the one described by Liu et al. [citation]. The text decoder of the above methods generates text in a left-to-right reading order, where the former predicted words are input into the neural network to generate the next word.

### Non-autoregressive Models
Unlike the autoregressive methods aforementioned, non-autoregressive methods predict each word independently of previously generated ones. Fei [citation] proposed a look-back mechanism that is introduced for variable refinement and faster caption generation. Yu et al. [citation] greatly improve the performance by devising the model with the Swin-Transformer and a semantic retrieval method to increase the decoder scale. SAIC [citation] 
 makes a trade-off between captioning speed and model performance by a semi-autoregressive model.

Most recently, a non-autoregressive method called diffusion models, first proposed in [citation], has had a huge success in image generation [citation]. Depending on the data type, diffusion models can be divided into continuous diffusion models [citation] and discrete diffusion models [citation]. On one hand, based on the continuous diffusion models, Bit Diffusion [citation] first projects tokens into continuous space and generates captions. SCD-Net [citation] further improves Bit Diffusion by better visual-language alignment through cascaded transformer blocks. On the other hand, DDCap [citation] first utilizes a discrete diffusion model with a CLIP [citation] image encoder in the image captioning task. All approaches mentioned above extract the continuous image representation before serving as conditions to generate captions. While our work similarly adopts discrete diffusion modeling, we depart from prior techniques that encode images into continuous features. Instead, we condition the diffusion process on discrete image tokens, establishing a unified discrete-to-discrete alignment framework that explicitly bridges visual and textual semantics.

## Methodology

### Masked Conditional Diffusion Model
#### Model Structure
As shown in Figure [reference], given an image, the VQ-VAE encoder first encodes the image into latent representations. Then it maps this representation with the closest embedding in the Codebook. The discrete diffusion text decoder contains several transformer blocks. The decoder achieves multimodal feature fusion in the cross-attention layer. Furthermore, the Masked Condition Strategy (MCS) is applied to randomly mask some discrete image features before serving as the conditions. Given the ground truth caption [x] and image feature [y], the MC-Diffusion aims to maximize [p(x|y)].

[Figure: Overall framework of Masked Conditional Diffusion Model (MC-Diffusion). MC-Diffusion includes: (a) VQ-VAE to extract discrete image features. (b) Masked condition strategy (MCS) to mask random image features. (c) Discrete diffusion decoder to denoise the caption sequence.]

#### VQ-VAE Image Encoder
MC-Diffusion begins with a VQ-VAE to extract discrete image features, represented as [y R^{h w}] and reshaped into a vector [y={y_1,y_2,...,y_N}], where [N=h w] and [(h,w)] denotes the encoded image feature size.

#### Discrete Diffusion Forward Process
Unlike continuous diffusion models that corrupt an image by gradually injecting Gaussian noise, discrete diffusion models corrupt text by randomly replacing some tokens with other tokens or the [MASK] token [citation]. Specifically, consider the one-hot version of a token [x_{t-1} R^{1 (M+1)}], where [t] denotes the time step, and [M] the vocabulary size. The forward process can be parameterized by a transition matrix [Q_t^{(M+1) (M+1)}] and [[Q_t]_{ij}=q(x_t=j|x_{t-1}=i)]. To reduce ambiguity, [X_t] denotes the random variable and [X_t=x_t] its realisation. The one-step forward process is defined as
[
 q(X_t|X_{t-1}=x_{t-1})=x_{t-1} Q_t R^{1 (M+1)}.
 
]
Notably, [x_{t-1}] represents a single token; we assume that the transition equation Eq. ([reference]) is applied to each token independently. Similar to the continuous diffusion process, [t]-step transition can also be parameterized directly from [x_0] as
[
 q(X_t|X_0=x_0)=x_0 {Q}_t R^{1 (M+1)}, with {Q}_t=Q_1Q_2...Q_t.
 
]
There are multiple choices for the transition matrix [Q_t]. Here we follow Mask-and-replace diffusion strategy from VQ-Diffusion [citation]:
equation*
 Q_t=
 pmatrix
 _t+_t & _t & _t & & 0 \\
 _t & _t+_t & _t & & 0 \\
 _t & _t & _t+_t & & 0 \\
 & & & & \\
 _t & _t & _t & & 1 \\
 pmatrix
equation*
This transition matrix can be interpreted as follows: an additional [MASK] token is introduced, each token has a probability of [_t] to be replaced by [MASK] token, a probability of [_t] to transfer to another token in the vocabulary, and a probability of [_t=1-M_t-_t] to be unchanged. 

#### Discrete Diffusion Reverse Process
 Given the max timestep [T] (a hyperparameter). Starting from the random tokens (noise) [x_t] at timestep [t=T], the discrete diffusion reverse process removes the [MASK] and corrects wrong tokens progressively. The one-step reverse process is formulated as
align
q(X_{t-1}|X_t=x_t,y)&=q({X_{t-1},X_t=x_t|y)}{q(X_t=x_t|y)} \\
&=_{x_0}q(X_{t-1}|X_t=x_t,X_0=x_0,y)q(X_0=x_0|X_t=x_t,y)\\
&_{x_0}q({X_{t-1}|X_t=x_t,X_0={x}_0)}_{Posterior}p_{(X_0={x}_0|X_t=x_t,y)}_{Neural Network}.

align
The approximation holds because [q(X_0=x_0|x_t=x_t,y)] is not accessible but can be approximated with neural network [p_{}(X_0={x}_0|X_t=x_t,y)]. [{x}_0] represents [{x}_0(x_t,y)] for simplicity. [{x}_0(x_t,y)] is the noiseless token at time [0] predicted by neural network conditioned on [x_t] and [y].The posterior is
align*
 q(X_{t-1}|X_t=x_t,{X}_0={x}_0)&=q({X_t=x_t|X_{t-1},{X}_0={x}_0)q(X_{t-1}|{X}_0={x}_0)}{q(X_t=x_t|{X}_0={x}_0)} \\
 &={x_t Q_t^ {x}_0{Q}_{t-1}}{{x}_0 {Q}_tx_t^},
align*
where [] denotes element-wise multiplication.
In sum, given the max timestep [T], the reverse process samples a random token sequence [x_t] at timestep [t=T] and extracts discrete image features [y]. Subsequently, for each timestep from [t=T] to [t=1], the sequence [x_{t-1}] is computed recursively based on the current state [x_{t}] and features [y] according to Eq. ([reference]). This iterative refinement continues until the final noiseless output [x_{0}].

#### Loss Function
We follow D3PM [citation] to minimize the variance lower bound plus an auxiliary loss which encourages good predictions of the data [x_0]:
align
 L=E[D_{KL}(q(x_{t-1}|x_t,x_0) p_(x_{t-1}|x_t))]+[ p_(x_0|x_t,y)],
 
align
where [D_{KL}] denotes the Kullback-Leibler divergence.

### Masked Condition Strategy
Diffusion models enable sampling random data points from the learned distribution [p(x)]. To control the generated data explicitly (e.g., generate relevant captions for a given image), guidance methods have been studied in the context of image generation. In the following, we first introduce classifier-free guidance [citation] (Definition [reference]). Then we describe Masked Condition Strategy (MCS) (Definition [reference]), our simple but effective guidance method to achieve fine-grained visual-language alignment.
definition[Classifier-free Guidance [citation]]
 
 Given a conditional model [p(x_t|y)] and an unconditional model [p(x_t)], the classifier-free guidance combines their score functions via a linear interpolation controlled by a guidance scale [ 0]:
 align*
 _{x_t} p(x_t|y)
 :&=(1-)_{x_t} p(x_t)+_{x_t} p(x_t|y), 
 align*
 where [x_t] is the noised sample at timestep [t] and [y] is the condition.
definition

A higher [] value indicates that the model takes more account of conditional information, with [=1] representing a fully conditional diffusion model. In the training step, the conditional and unconditional models are trained in one model by randomly replacing [P_{cond}] of the condition with zeros. It has shown the trade-off between visual-language alignment and language fidelity in image captioning [citation]. 

Classifier-free guidance achieves coarse-grained visual-language alignment, which fails to capture localized semantics. MCS achieves fine-grained visual-language alignment by not removing the entire condition information, but masks partial condition information. To achieve this, each condition feature [y_i y={y_1,y_2,...,y_N}] has a probability [P_{mask}] to be masked:
[
 
 y_i = cases
 [MASK], & p P_{mask} \\
 y_i, & p > P_{mask}
 cases
]
where [p] is a random number sampled from [U(0,1)]. 
definition[Masked Condition Strategy (MCS)]
 
 Given a partial conditional model [p(x_t|y_{[M]},y_{o})] and a conditional model [p(x_t|y)], the MCS combines their score functions via a linear interpolation controlled by a guidance scale [ 0]:
 align*
 _{x_t} p(x_t|y)&:= _{x_t} p(x_t|y_{[M],y_{o}}) +(1-)_{x_t} p(x_t|y),
align*
 where [y_{[M]}] denotes the masked condition feature and [y_{o}] represents the condition feature not been masked.
definition

Similar to classifier-free guidance, [] controls how much we care about the condition information. As Algorithm 1 shows, in the training period, the two models [_{x_t} p(x_t|y)] and [_{x_t} p(x_t|y_{[M],y_{o}})] are trained in one model by masking the condition in some of the data in the dataset while leaving others fully conditioned.

By masking partial condition information, the model is trained to align different image features with text at each time step. Hence, this strategy forces the neural network to establish fine-grained visual-language alignment.
algorithm
 Training of the MC-Diffusion with MCS
 algorithmic
 Condition rate [P_{{cond} [0,1]] and mask rate [P_{mask}]}
 
 (image, caption)[] sampled from the training dataset 
 [t U({1,...,T})] sample a time step [t]
 [x_0] CLIP text embedding(caption), [y] VQ-VAE image Encoder(image)
 [x_t] add noise to [x_0] [] Eq. ([reference])
 random number p [] sampled from [U(0,1)]
 [p<P_{{cond}]}
 [(y_{[M]},y_{o})]mask some entries in condition [y] [] Eq. ([reference])
 [({x}_0, x_{t-1})] discrete diffusion decoder ([y_{[M]},y_{o},x_t]) [] Eq. ([reference])
 Loss [({x}_0, x_{t-1},x_0)] [] Eq. ([reference])
 
 [({x}_0, x_{t-1})] discrete diffusion decoder ([y,x_t])
 Loss [({x}_0, x_{t-1},x_0)] [] Eq. ([reference])

 converged
 algorithmic
algorithm
#### Further Explanation on Masked Condition Strategy If we further make some derivation on our MCS:
align*
 _{x_t} p(x_t|y)
 &= _{x_t} p(x_t|y_{[M],y_{o}})+(1-)_{x_t} p(x_t|y)\\
 &=[_{{x_t}p(y_{[M]}|x_t,y_{o})}_{Image Inpainting Model}+_{{x_t}p(x_t|y_{o})}_{Partial Conditioned Model}]\\
 &+(1-)_{x_t} p(x_t|y).
align*
We can alternatively view the MCS as implicitly learning an image inpainting model [_{x_t}p(y_{[M]}|x_t,y_{o})], a partial conditioned model [_{x_t}p(x_t|y_{o})] and a fully conditioned model [_{x_t} p(x_t|y)]. The implicit image inpainting model predicts the masked image features [y_{[M]}] using the non-masked image features [y_{o}] and the caption [x_{t}], which enables fine-grained visual-language alignment. The partial caption model and the fully conditioned model learn to generate the caption with different amounts of conditional information, which improves the performance of the denoising neural
network.

## Experiments

### Implementation Details
Experiments are conducted on the CUB-200 [citation] dataset. It contains over 8k training images and 3k
test images. Each image includes 10 captions. The average caption length is 14.2 tokens. VQ-VAE image encoder comes from the VQGAN [citation] with Codebook size [K=2886]. It extracts 32[]32 discrete features from 256[]256 images. Our diffusion decoder contains 18 transformer blocks with dimension [d=512]. The model includes 122M trainable parameters. As for classifier-free guidance and MCS, we set the condition rate [P_{cond}] and condition mask rate [P_{mask}] to 0.1. We set the diffusion step [T=100]. MC-Diffusion is optimized by AdamW [citation] with parameter [=(0.9,0.96)]. The beginning learning rate is 1.0e-6 and increases to 4.5e-4 after 1000 warmup steps. The batch size is 128, and the training epoch is set to 200.

### Evaluation Metrics
#### Reference-based Metrics
Reference-based metrics evaluate the similarity between the generated and ground-truth captions. BLEU [citation] and ROUGE [citation] compare the overlapping n-grams, and Meteor [citation] further considers the accuracy and recall over the entire corpus. CIDEr [citation] uses Term Frequency-Inverse Document Frequency (TF-IDF) to assess the importance of each token. Unlike the above-mentioned metrics, SPICE [citation] and RefCLIPScore [citation] assess the underlying connection with pre-trained models. 

#### Reference-free Metric
Reference-free metric computes the similarity between the generated caption and the image. CLIPScore [citation] leverages the CLIP ViT-B/32 [citation] model to extract CLIP embeddings of the generated caption [c] and image [i]. CLIPScore is defined as [CLIPScore=2.5((c,i),0)].

### Baselines
Source Pre-trained and DCC [citation] are two autoregressive baselines with an long short-term memory (LSTM) [citation] text decoder. ATCIC [citation] is the state-of-the-art model on the CUB-200 dataset. We select Bit Diffusion [citation] as non-autoregressive baseline. All autoregressive approaches are pre-trained on the MSCOCO dataset [citation], while MC-Diffusion only contains a pre-trained VQ-VAE image encoder. Furthermore, we compare MCS with classifier-free guidance with different guidance scales [].

### Results
#### Performance Comparisons
Table [reference] shows the performance comparison without the MCS. MC-Diffusion outperforms autoregressive baselines across all metrics. Specifically, the Meteor and SPICE are 103.0\

[Table]
[Table]
[Table]
[Table]

[Figure: Performance comparison on different guidance scales []. In each subplot, the vertical axis represents the reference-free metric CLIPScore, while the horizontal axis represents various reference-based metrics. As the reference-based metrics increase, it can be significantly observed that the MCS shows a much smaller decline in the reference-free metric (CLIPScore) compared to classifier-free guidance.]

Table [reference] further illustrates some examples generated by MC-Diffusion. MC-Diffusion can produce more descriptive and longer captions compared to ground-truth captions. As shown in the second image, none of the ground-truth captions point out that the bird has black feathers covering the top, except MC-Diffusion. However, the text generated by MC-Diffusion may contain more grammatical errors (e.g., ``in with a all'' in the first image caption result of Table [reference]) and have less fluent sentence structure.

#### Masked Condition Strategy
Table [reference] and Table [reference] compare the results of classifier-free guidance and MCS on the same MC-Diffusion with different guidance scales []. As the guidance scale [] increases, if [ 3], both classifier-free guidance and MCS exhibit a trade-off between the reference-based and reference-free metric. However, when [>3], the higher guidance scale may result in higher distribution shift, deteriorating both reference-based and reference-free metrics. To compare classifier-free guidance and MCS more intuitively, we plot the results in the tables as Figure [reference]. As the reference-based metrics increase, it can be significantly observed that the MCS shows a much smaller decline in the reference-free metric (CLIPScore) compared to classifier-free guidance. This improvement can be attributed to the partial masking of the image features. It enables finer-grained visual-language alignment while demonstrating superior capability in model guidance.

## Conclusion

In this work, we dive into the idea of devising the visual-language alignment in diffusion models for image captioning. We propose a masked conditional diffusion model (MC-Diffusion) to establish discrete-to-discrete alignment. The Masked Condition Strategy (MCS) is further proposed to achieve fine-grained visual-language alignment. We validate the MC-Diffusion against the baselines and state-of-the-art methods on the CUB-200 dataset. We also compare the performance of the MCS and classifier-free guidance on different guidance scales. We are happy to see that MC-Diffusion achieves a higher CLIPScore (better visual-language alignment) while MCS improves reference-based metrics with minimal hurt on CLIPScore. For future work, since classifier-free guidance also presents a trade-off between image fidelity and diversity in the text-to-image task, we can test whether the MCS performs better in this aspect as well.

