# Optimal Algorithms for Online Convex Optimization with Adversarial Constraints

**Authors**: Abhishek Sinha, Rahul Vaze \\
 School of Technology and Computer Science \\
 Tata Institute of Fundamental Research \\
 Mumbai 400005, India \\
 {abhishek.sinha@tifr.res.in

## Abstract

A well-studied generalization of the standard online convex optimization (OCO) framework is constrained online convex optimization (COCO). In COCO, on every round, a convex cost function and a convex constraint function are revealed to the learner after it chooses the action for that round. The objective is to design an online learning policy that simultaneously achieves a small regret while ensuring a small cumulative constraint violation (CCV) against an adaptive adversary interacting over a horizon of length $T$. A long-standing open question in COCO is whether an online policy can simultaneously achieve $O(T)$ regret and $O(T)$ CCV without any restrictive assumptions. For the first time, we answer this in the affirmative and show that a simple first-order policy can simultaneously achieve these bounds. Furthermore, in the case of strongly convex cost and convex constraint functions, the regret guarantee can be improved to $O( T)$ while keeping the CCV bound the same as above.
We establish these results by effectively combining adaptive OCO policies as a blackbox with Lyapunov optimization - a classic tool from control theory. Surprisingly, the analysis is short and elegant.

---

## Introduction

Online convex optimization (OCO) is a standard framework for modelling and analyzing a broad family of online decision problems under uncertainty. In the OCO problem, on every round [t], an online policy first selects an action [x_t] from a closed and convex admissible set (*a.k.a.* decision set) [X.] Then the adversary reveals a convex cost function [f_t], resulting in a cost of [f_t(x_t)]. 
The goal of an online policy is to choose an admissible action sequence [{x_t}_{t=1}^T] so that its cumulative cost is not much larger than that of any fixed admissible action chosen in hindsight. In particular, the objective is to minimize the static regret defined below

eqnarray 
	Regret_T _{{f_t}_{t=1}^T} _{x^ X} Regret_T(x^), where Regret_T(x^) _{t=1}^T f_t(x_t) - _{t=1}^T f_t(x^).
eqnarray
 The term *static* refers to using a fixed benchmark, specifically only one action [x^] throughout the horizon of length [T]. 
 
 In this paper, we consider a generalization of the standard OCO framework. In this problem, on every round [t,] the online policy first chooses an admissible action [x_t X,] 
 and then the adversary chooses a convex cost function [f_t: X R] and [k] constraints of the form [g_{t,i}(x) 0, \ i [k],] where [g_{t,i}: X R] is a convex function for each [i [k]]Notations: For any natural number [n], we define [[n] {1,2,, n\.] For any real number [z], we define [(z)^+ (0,z).]}. Since [g_{t, i}]'s are revealed after the action [x_t] is chosen, an online policy need not necessarily take feasible actions on each round, and the obvious metric of interest in addition to intro-regret-def is the total cumulative constraint violation (CCV) [V(T)] defined as 
 
 eqnarray 
 	CCV_T V(T) = _{i=1}^k V_i(T) where V_i(T) = _{t=1}^T (g_{t,i}(x_t))^+. 
	eqnarray
Let [X^] be the feasible set consisting of all admissible actions that satisfy all constraints [g_{t,i}(x) 0, \ i [k], t [T]]. Under the standard assumption that [X^] is not empty, the goal is to design an online policy to simultaneously achieve a small regret intro-regret-def with respect to any admissible benchmark [x^ X^] and a small CCV intro-gen-oco-goal. We refer to this problem as the constrained OCO (COCO). The assumption [X^ ] will be relaxed in Section [reference] for the Online Constraint Satisfaction (OCS) problem where the cost functions are set to zero, and the objective is to minimize just the CCV.

COCO arises in many applications, including online portfolio optimization with risk constraints, resource allocation in cloud computing with time-varying demands, pay-per-click online ad markets with budget constraints [citation], online recommendation systems, dynamic pricing, revenue management, robotics and path planning problems, and multi-armed bandits with fairness constraints [citation]. 

The necessity for revealing the constraints sequentially may also arise, *e.g.,* in communication-limited settings, where it might be infeasible to reveal all constraints defining the feasible set at a time (*e.g.,* combinatorial auctions). See Section [reference] for an application of the COCO framework in fraud detection which involves binary classification with a highly-imbalanced dataset. 

 The {Hidden Set Problem:}
Let [X] be an *admissible* set of actions which is known to the policy. Let [X^], called the *feasible* set, be a closed and convex subset of [X]. Due to a large number of defining constraints, the feasible set [X^] is too complex to communicate to the policy *a priori*. However, an efficient separation oracle for [X^] is assumed to be available. On the [t]th round, the policy first selects an admissible action [x_t X] and then, the adversary reveals a convex cost function [f_t] and *some* convex constraint of the form [g_t(x) 0,] which contains the unknown feasible set [X^]. As an example, the constraints could come from the separation oracle that, if [x_t] is infeasible, outputs a hyperplane separating the current action [x_t X] and the hidden feasible set [X^]. The objective of the policy is to perform as well as any action from the hidden feasible set [X^] in terms of the regret and the cumulative constraint violation metrics. 
 
 [Figure: {Illustrating the {Hidden Set]

## The Constrained OCO (COCO) Problem

In this section, we generalize the [] and the usual unconstrained OCO and consider the COCO where
 on each round [t, t=1, , T] an online policy first chooses an admissible action [x_t X] 

 and then the adversary chooses a convex cost function [f_t: X R] and a constraint of the form [g_t(x) 0,] where [g_t: X R] is a convex function.For notational simplicity, in this section, we assume that only one constraint function is revealed on each round (*i.e.,* [k=1]). The general case of [k>1] can be handled similarly as in Section [reference]. Let [X^] be the feasible set satisfying all constraints as defined in Assumption [reference]. Then, the objective is to simultaneously minimize the regret and the CCV as defined in intro-regret-def and intro-gen-oco-goal with [k=1], respectively. 

 The COCO can be motivated by the following offline convex optimization problem where the functions [{f_t, g_t}_{t=1}^T] are known *a priori*: 
 
 eqnarray*
 	 _{t=1}^T f_t(x),
 eqnarray*
subject to the constraints
 eqnarray*
 	g_t(x) 0, t [T], 
 	x X.
 eqnarray*
 
 Since [(g_t(x_t))^+ 0,] intro-gen-oco-goal uses a stronger definition of CCV compared to the [] (c.f. violation-def1), where the strict feasibility at some round may compensate for infeasibility in other rounds [citation]. With abuse of notation, from here onwards, we redefine the convex constraint functions as [g_t(x) (g_t(x))^+, x X, t 1]. In other words, the constraints are pre-processed by passing them through the standard ReLU unit, ensuring that [g_t(x) 0, x X, t 1.]

## Strongly Convex Constraints

In this section, we investigate the case when each constraint function [2(g_t())] are []-strongly convex. To establish strong results without any extraneous assumptions, we first consider the case when the cost functions are identically equal to zero, and the only objective is to derive strong bounds for the queue length variables. 

By setting [f_t=0, t,] we immediately have [Regret_t(x^)=0.] Hence, strong-cvx-regret yields the following recursive bounds on the queue length process;
eqnarray 
	Q^2(t) G^2{4} _{=1}^t Q^2(){_{s=1}^ Q(s)}.
eqnarray

The following result gives a strong bound on the queue lengths as implied by the above bound. 
framed
theorem[(Upper bound on the queue length)]
For []-strongly convex constraint functions [g]'s, the queue length process is bounded as [Q(t)=O(G^2{4} (t)), t 1.]
theorem
framed
See Proposition [reference] in the Appendix for the proof of the above result.

## Strongly Convex Constraints

Clearly, in this case each surrogate cost function [f_t'], defined in surrogate-def, is [(V+Q(t))]-strongly convex 
 with the norm of the (sub)gradients bounded by [G_t (V+Q(t))G{2}] grad-bd. Hence, using the regret bound strong-cvx-regret, there exists an OGD policy that achieves the following bound:
 
 eqnarray 
 	Q^2(t) + V Regret_t(x^) G^2{4}_{=1}^t V^2+ Q^2(){V+ _{s=1}^ Q(s)}.
 eqnarray

## The Online Constraint Satisfaction Problem (\textsc{OCS

)} 

In this section, we study
a special case of the COCO problem, which involves only constraint functions and no cost functions. The OCS problem arises in many practical settings, including the multi-task learning problem (see Section [reference] in the Appendix for a brief discussion). In Section [reference] in the Appendix, we also establish a connection between the OCS problem and the well-studied Convex Body Chasing problem [citation]. The setup is similar to the COCO setting -- on every round [t 1], an online policy selects an action [x_t] from a closed, bounded, and convex admissible set [X R^d]. After observing the current action [x_t], the adversary chooses [k] constraints of the form [g_{t,i}(x) 0, i [k],] where each [g_{t,i}: X R ] is a convex function. 
 Let [I] be any sub-interval of the horizon [[1,T].] The cumulative constraint violation (CCV) [V(T)] for the OCS problem is defined as the maximum *signed* cumulative constraint violation in any sub-interval:
 eqnarray 
		V(T) = _{i=1}^k V_i(T), where V_i(T) = _{I [1,T]}_{t I} g_{t,i}(x_t), 1 i k.
eqnarray
The objective is to design an online learning policy so that [V(T)] is as small as possible.
It is worth noting that in the [] problem, we consider a soft constraint violation metric [_{I}_{t I} g_{t,i}(x_t)] instead of the hard violation metric [_{t=1}^T (g_{t,i}(x_t))^+] as in COCO. This allows for compensating the infeasibility on one round with strict feasibility on other rounds.

In contrast with the COCO setting, without Assumption [reference], running a no-regret policy on the pointwise maximum of the constraint functions no longer works as the CCV of any fixed benchmark could grow linearly with 

[T]. In the OCS problem, we relax the feasibility assumption (Assumption [reference]), and consider the following two distinct alternatives instead. 
 1. [S]-feasibility: Here, we assume that there is an admissible action [x^ X] that satisfies the aggregate constraints over any interval of [S] rounds. However, unlike [citation], which also considers the same assumption, the value of the parameter [S] is not necessarily known to the policy *a priori*. Towards this end, we define the set of all [S]-feasible actions [X_S] as below: 
eqnarray 
X_S ={x^ X: _{ I} g_{,i}(x^) 0, sub-intervals I [1,T], |I| = S, i [k]}. 
eqnarray
We now replace Assumption [reference] with the following weaker version:
assumption[[S]-feasibility] 
	[X_S ] for some [1 S T.]
assumption

Clearly, Assumption [reference] is weaker than Assumption [reference] as [X^ X_S, S 1.] Note that even when the individual constraint functions satisfy [S]-feasibility, their pointwise maximum need not satisfy [S]-feasibility. Hence, unlike COCO under Assumption [reference], this problem cannot be solved by simply running a no-regret policy on the pointwise maximum of the constraints. 

 2. [P_T]-constrained adversary
In this case, we drop any feasibility assumption altogether. As a consequence, any static admissible benchmark [x^ X] also incurs a CCV. 
definition 

An adversary is called [P_T]-constrained if its minimum static CCV is [P_TF], *i.e.,* 
[ 1{F} _{x^ X} _{I [T],i} _{t I} g_{t,i}(x^) = P_T], where [F] is a normalizing factor denoting the maximum absolute value of the constraint functions within the compact admissible set [X]. 
definition
As before, the value of [P_T] is not necessarily known to the policy *a priori*.

## Experiments: Credit Card Fraud Detection

[Figure: ROC curve obtained by varying []]
{Classification with a highly imbalanced dataset:
We first formulate the credit card fraud detection problem in the COCO framework. 

Assume that we receive a sequence of [d]-dimensional feature vectors [{z_t}_{t 1}] and the corresponding binary labels [{y_t}_{t 1}] for a sequence of credit card transactions, where each transaction can either be legitimate (label [=0]) or fraudulent (label [=1]). The problem is to predict the label [y_t] for each transaction [z_t] before its true label [y_t {0,1}] is revealed. Typically, legitimate transactions outnumber fraudulent transactions by orders of magnitude. Since the goal is to detect any fraudulent transactions (even at the cost of a few false alarms), maximizing the classification accuracy alone is insufficient due to the significant class imbalance. We propose the following reformulation for this problem within the COCO framework. 

Formulation: Let [y_t(z_t,x)] be the likelihood of class [1] for the feature [z_t,] given by a parameterized model with parameter [x]. Hence, the log-likelihood [L(t)] of the data on round [t] can be expressed as: 
[Equation]
We train the model by maximizing the sum of log-likelihoods for legitimate transactions, subject to the constraint that all fraudulent transactions have a likelihood value close to [1] (*i.e.,* the sum of the log-likelihoods of the fraudulent transactions remains close to zero):
eqnarray 
 _x _{t=1}^T (1-y_t) (1-y_t(z_t, x)), s.t. _{t=1}^T y_t (y_t(z_t, x)) 0.
eqnarray

The above problem prob1 can be immediately recognized to be an instance of COCO with the following cost and constraint functions:
[ f_t(x) -(1-y_t) (1-y_t(z_t,x)), g_t(x) -y_t (y_t(z_t,x)), t 1.]
In our experiments, we consider the common scenario in which the likelihoods are modeled by the output of a feedforward neural network. Note that the feasibility assumption (Assumption 3) is naturally satisfied as the overparameterized neural network models are known to perfectly fit the data [citation]. However, in this case, the functions [f_t] and [g_t] are generally non-convex. 

Experiments:

We experiment with a publicly available credit card transaction dataset [citation]. This highly imbalanced dataset contains only [492] frauds ([ 0.17\

Each data point has ]D_{in}=30[ features and binary labels. We choose a simple network architecture with a single hidden layer containing ]H=10[ hidden nodes and sigmoid non-linearities. Unlike previous algorithms, our algorithm is especially suitable for training neural network models as it only needs to compute the gradients (via backward pass) and evaluate the functions (via forward pass). Initially, all weights are independently sampled from a standard normal distribution. The network is then trained using Algorithm [reference] on a quad-core CPU with 8 GB RAM. The projection operation corresponds to ]L_2[-normalization. The code has been publicly released [citation]. 

Results:

Given the severe class imbalance, the area under the ROC curve, which plots the True Positive Rate (TPR) against the False Positive Rate (FPR), is an appropriate metric to evaluate any prediction algorithm for this problem. By varying the hyperparameter ][, we obtain the ROC curve shown in Figure [reference]. The area under the ROC curve is computed to be ] 0.92[, which is an excellent score (cf. ideal score ]=1.0$), notwithstanding the fact that, unlike the standard resampling-based techniques, the algorithm learns in an entirely online fashion starting from random initialization. Figure [reference] illustrates the expected sublinear variation of CCV during one of the algorithm runs.

## Conclusion

An interesting open question is whether the assumption of the feasibility of the constraints on every slot can be suitably relaxed and still ensure sublinear regret and constraint violation penalties. Specifically, it would be interesting to extend our results to the [K]-benchmark case [citation] where the cumulative constraints hold for any consecutive [K] intervals where [K] is a sublinear function of the time-horizon [T], *i.e.,*
eqnarray*
	_{ I}g_ (x^) 0
eqnarray*
for all intervals [|I| =K (T)] where [()] is a sublinear function. Secondly, proving joint lower bounds for static regret and constraint violation penalty would be interesting. Throughout this paper, we use the quadratic potential function to design our online policy. However, our regret decomposition result is general and could be used with any reasonable potential function. It would be interesting to see if improved performance guarantees can be established by choosing a different potential function.

In this paper, we proposed efficient online policies for the COCO problem with optimal performance bounds. We also derived sublinear CCV bounds for the OCS problem under a set of relaxed assumptions. Our analysis is streamlined, leveraging Lyapunov theory and adaptive regret bounds for the standard OCO problem. 
In the future, exploring dynamic regret bounds and a bandit extension of the COCO problem would be interesting.

## Acknowledgement

This work was supported by the Department of Atomic Energy, Government of India, under project no. RTI4001 and by a Google India faculty research award. The first author was also partially supported by a US-India NSF-DST collaborative grant coordinated by IDEAS-Technology Innovation Hub (TIH) at the Indian Statistical Institute, Kolkata. The authors gratefully acknowledge comments from the anonymous reviewers, which substantially improved the quality of the presentation.

## Appendix



