# Doubly-Bounded Queue for Constrained Online Learning:
	\ Pace with Dynamics of Both Loss and Constraint

**Authors**: Juncheng Wang{Corresponding author, jcwang@comp.hkbu.edu.hk

**Affiliation**: Department of Computer Science, Hong Kong Baptist University

## Abstract

We consider online convex optimization with time-varying constraints and conduct performance analysis using two stringent metrics: dynamic regret with respect to the online solution benchmark, and hard constraint violation that does not allow any compensated violation over time. We propose an efficient algorithm called Constrained Online Learning with Doubly-bounded Queue (COLDQ), which introduces a novel virtual queue that is both lower and upper bounded, allowing tight control of the constraint violation without the need for the Slater condition. We prove via a new Lyapunov drift analysis that COLDQ achieves $O(T^1+V_x{2})$ dynamic regret and $O(T^{V_g})$ hard constraint violation, where $V_x$ and $V_g$ capture the dynamics of the loss and constraint functions. For the first time, the two bounds smoothly approach to the best-known $O(T^1{2})$ regret and $O(1)$ violation, as the dynamics of the losses and constraints diminish. For strongly convex loss functions, COLDQ matches the best-known $O(T)$ static regret while maintaining the $O(T^{V_g})$ hard constraint violation. We further introduce an expert-tracking variation of COLDQ, which achieves the same performance bounds without any prior knowledge of the system dynamics. Simulation results demonstrate that COLDQ outperforms the state-of-the-art approaches.

---

## Introduction

In many online learning applications, optimization losses and constraints are dynamic over time. Online Convex Optimization (OCO) [citation], as the intersection of learning, optimization, and game, is a vital framework for solving online learning problems under uncertainty. It has broad applications such as advertisement placement [citation], load balancing [citation], network virtualization [citation], and resource allocation [citation].

In the standard OCO setting, a learner selects online decisions from a known convex set to minimize a sequence of time-varying convex loss functions. The information of each loss function, however, is only revealed to the learner after the decision has been made. Given this lack of current information, the objective of the learner becomes to minimize the *regret*, which is the accumulated difference between the losses incurred by their online decisions and those of some benchmark solutions. [citation] considered both *static* regret to an offline benchmark and *dynamic* regret to an online benchmark. The proposed online projected gradient descent algorithm provided a dynamic regret bound that *smoothly* approaches to [O(T^1{2})] static regret, as the accumulated variation of the loss functions reduces, the OCO algorithm keeps pace with the dynamics of the losses.

The projection operation to strictly satisfy the constraints at each time can incur heavy computation. Furthermore, in many applications, the online decisions are subject to constraints that are allowed to be violated at certain time slots. [citation] initiated the study on OCO with *soft constraint violation*, which measures the amount of compensated violations over time. In contrast, with a goal to limit the instantaneous violation, [citation] introduced a stronger notion of *hard* constraint violation that does not allow any compensated violation over time. For *fixed* constraints, the best-known soft and hard constraint violation bounds are both [O(1)] [citation].

Most existing works on OCO with *time-varying* constraints focused on the static regret [citation]. Dynamic regret for time-varying constrained OCO was more recently studied [citation]. As the accumulated variation of the constraint functions reduces, the best-known soft and hard constraint violation bounds for time-varying constraints approach to [O(T^1{2})] and [O(T^1{2} T)], respectively [citation]. However, none of the constraint violation bound recovers the best-known [O(1)] violation for fixed constraints, the constrained OCO algorithms do *not* keep pace with the dynamics of the constraints.

The above discrepancies motivate us to pose the following key question: *Can a constrained OCO algorithm provide a dynamic regret bound and a constraint violation bound that smoothly approach to the best-known [O*(T^{1{2})] regret and [O(1)] violation, respectively, as the dynamics of the losses and constraints diminish?} Our answer is yes.

**Contributions.** We summarize our contributions below.

- We propose an effective algorithm named Constrained Online Learning with Doubly-bounded Queue (COLDQ) for tackling OCO problems with time-varying constraints. Existing virtual-queue-based approaches rely on either a lower or an upper bound of the virtual queue to bound the constraint violation. In contrast, we introduce a novel virtual queue that enforces both a lower and an upper bound, without the commonly assumed Slater condition, to strictly control the constraint violation.
	
	 We analyze the performance of COLDQ via a new Lyapunov drift design that leverages both the lower and upper bounds of the virtual queue. We show that COLDQ provides [O(T^1+V_x{2})] dynamic regret and [O(T^{V_g})] hard constraint violation, where [V_x] and [V_g] capture the dynamics of the losses and constraints (see definitions in (eq:Vx) and (eq:Vg)). For the first time, the two bounds smoothly approach to the best-known [O(T^1{2})] regret and [O(1)] violation as [V_x0] and [V_g0].
	
	 When the loss functions are strongly convex, we show that COLDQ matches the best-known [O(T)] static regret, while maintaining the [O(T^{V_g})] hard constraint violation. We further propose a variation of COLDQ with expert tracking that can achieve the same [O(T^1+V_x{2})] dynamic regret and [O(T^{V_g})] hard constraint violation, without any prior knowledge about the system dynamics.
	
	 We conduct experiments to evaluate the practical performance of COLDQ on various applications involving both time-varying and fixed constraints. Numerical results confirm the effectiveness of COLDQ over the state-of-the-art approaches.

[Table]

[Table]

## Related Work



## Constrained Online Convex Optimization

We can consider the constrained OCO problem as an iterative game between a learner and the system over [T] time slots. At each time [t], the learner first selects a decision [x_t] from a known feasible set [X^p]. The loss function [f_t(x):R^p] and the constraint function [g_t(x)=[g_t^1(x),,g_t^N(x)]^:R^p^N] are then revealed to the learner, incurring a loss of [f_t(x_t)] and a constraint violation of [g_t(x_t)]. Both the loss function [f_t(x)] and the constraint function [g_t(x)] are unknown a priori and are allowed to change arbitrarily over time.

The goal of the learner is to select from the feasible set an online decision sequence that minimizes the total accumulated loss under time-varying constraints. This gives rise to the following time-varying constrained OCO problem
[Equation]
When [g_t(x)=g(x),t], [**P**] becomes the OCO problem with fixed constraints.

## Constrained Online Learning with Doubly-bounded Queue (COLDQ)

We present the COLDQ algorithm for solving [**P**]. In COLDQ, we introduce a novel doubly-bounded virtual queue and a new Lyapunov drift design, which will be shown to provide improved regret and constraint violation bounds.

## Performance Bounds of COLDQ



## Experiments

We conduct experiments to evaluate the performance of COLDQ for both time-varying and fixed constraints. In the Appendix, we provide all the algorithm parameters used in our experiments, and detailed problem settings of the application to online job scheduling.

## Conclusions

We propose an effective COLDQ algorithm for OCO with time-varying constraints. We design a novel virtual queue that is bounded both from above and below to strictly control the hard constraint violation. Through a new Lyapunov drift analysis, COLDQ achieves [O(T^1+V_x{2})] dynamic regret and [O(T^{V_g})] hard constraint violation. For the first time, the two bounds smoothly approach to the best-known [O(T^1{2})] regret and [O(1)] violation, as the dynamics of the losses and constraints represented by [V_x] and [V_g] diminish. We further study the case of strongly-convex loss functions, and demonstrate that COLDQ matches the best-known [O(T)] static regret while maintaining the [O(T^{V_g})] hard constraint violation. Moreover, we extend COLDQ with expert tracking capability, which allows it to achieve the same dynamic regret and hard constraint violation bounds without any prior knowledge of the system dynamics. Finally, experimental results complement our theoretical analysis.

## Auxiliary Lemmas

lemma[Lemma 2.8 [citation]]
	*Let [X*] be a convex set. Let [f({x):X] be a [2]-strongly convex function with respect to a norm [], and [x^_{x}f(x)] be the optimal solution of [f(x)]. Then, we have [f(x^)f(x)--x^^2,].}
lemma
*Proof:* From the definition of strong convexity, we have for any [x,y]:
align*
	f(x)f(y)+(y),x-y+-y^2.
align*
Substituting [y=x^] into the above inequality and rearranging terms, we have for any [x]:
align*
	f(x^)f(x)-(x^),x-x^--x^^2.
align*
Further noting that the sufficient and necessary condition for [x^] to be a global optimal solution of the convex function [f(x)] is for any [x]:
align*
	(x^),x-x^0,
align*
we complete the proof.[]

lemma[Time Series]
	*The following time series is upper bounded for any [c[0,1)] as*
	align*
		_{t=1}^T1{t^c}1{1-c}T^{1-c}.
	align*
lemma
*Proof:* For any [c[0,1)], we have
align*
	_{t=1}^T1{t^c}_1^Tt^{-c}dt=1{1-c}t^{1-c}|_1^T=1{1-c}(T^{1-c}-1)1{1-c}T^{1-c}.
align*
[]

lemma[Lemma 1 [citation], Lemma 3 [citation]]
	*Let [X*] be a convex set. Let [{l_t({x):X}_{t=1}^T] be a sequence of convex functions. Assume [l_t(x)] is bounded, [F>0], such that [|l_t(x)|F,,t]. Let [M_+] and [>0] be constants. Let [{x_t[m]}_{t=1}^T,m={1,,M}] be [M] sequences of decisions. Then, for any given [w_1[m](0,1)] that satisfies [_{m=1}^Mw_1[m]=1], let [{x_t}_{t=1}^T] be a sequence of decisions updated via
		align*
			x_t=_{m=1}^Mw_t[m]x_t[m]
		align*
		where
		align*
			w_t[m]=w_{t-1[m]e^{-l_{t-1}(x_{t-1}[m])}}{_{m=1}^Mw_{t-1}[m]e^{-l_{t-1}(x_{t-1}[m])}}.
		align*
		Then, for any [T1], we have
		align*
			_{t=1}^Tl_t(x_t)-_{m}{_{t=1}^Tl_t(x_t[m])+1{}(1{w_1[m]})}{F^2T}{2}.
		align*
	}
lemma

*Proof:* See the proof of Lemma 1 in [citation].

## Proof of Lemma~\ref{lm:vq

}

*Proof:* We first prove [Q_t^n{},t,n] by induction. From the initialization of the virtual queue, we have [Q_1^n={},n]. Then, suppose [Q_{-1}^n{},n] for some [>1], we now prove [Q_^n{},n]. From the virtual queue updating rule 
([reference]), we consider the following two cases:
- If [(1-)Q_{-1}^n+[g_^n(x_)]_+>], we have
	align
		Q_^n&=(1-)Q_{-1}^n+[g_^n(x_)]_+(1-)Q_{-1}^n+|g_^n(x_)|(a){}(1-)G{}+G=G{}
	align
	where [(a)] follows from [Q_{-1}^n{}] by induction
	and the bound on [|g_t^n(x)|] in Assumption asm:G.
	
	 If [(1-)Q_{-1}^n+[g_^n(x_)]_+],
	we have
	align
		Q_^n=<G{}.
	align

Combining the above two cases, we have proven by induction that [Q_t^n{},t,n].

Further noting that [Q_1^n=,n] from initialization and [{Q}_t^n,t>1,n] from ([reference]), we complete the proof.[]

## Proof of Lemma~\ref{lm:drift

}

*Proof:* From the virtual queue updating rule in ([reference]), for any [t>1] and [n], we have
[Equation]
where [(a)] follows from[|{a,b}-b||a-b|,a,b0].

We now bound the RHS of ([reference]). For the second term on the RHS of ([reference]), we have[Equation]
where [(a)] follows from the triangle inequality, and [(b)] is because of the bound on [|g_t^n(x)|] in Assumption [reference] and the virtual queue upper bound in ([reference]).

For the third term on the RHS of ([reference]), we have
[Equation]
where [(a)] follows from the virtual queue upper bound in ([reference]),
and [(b)] is because [|[a]_+-[b]_+||a-b|].

For the last term on the RHS of ([reference]), we have
[Equation]
which follows form the virtual queue lower bound in ([reference]).

Substituting ([reference])-([reference]) into the RHS of
([reference]), for
any [t>1] and [n], we have
[Equation]

Rearranging terms of ([reference]), and summing over [n=1,,N], we have
[Equation]

From ([reference]) and noting that [_{n=1}^N|g_t^n(x_t)-g_{t-1}^n(x_t)|_{x}_t(x)-g_{t-1}(x)], we complete the proof. []

## Proof of Lemma~\ref{lm:fgt

}

*Proof:* Note that [_{t-1}(x_{t-1}),x-x_{t-1}]
is affine in [x] over [X], [_{n=1}^NQ_{t-1}^n[g_{t-1}^n(x)]_+] is convex in [x]
over [X] since the maximum and linear combination of convex functions
are also convex, and [_{t-1}-x_{t-1}^2] is [2_{t-1}]-strongly convex in [x] over [X]. Therefore, the objective function of [**P**_t] is [2_{t-1}]-strongly convex in [x] over [X]. Further noting that [x_t] is the optimal solution to [**P**_t], applying Lemma [reference] to [**P**_t], we have
[Equation]

We now bound the RHS of ([reference]). From the convexity of [f_{t-1}(x)], the first term on the RHS of ([reference]) is upper bounded by
[Equation]

From the definition of the dynamic benchmark [x_t^], the second term on the RHS of ([reference]) satisfies
[Equation]

For the last two terms on the RHS of ([reference]), we have
[Equation]
where [(a)] follows from [+b^2^2+^2-2] and [(b)] is because [{_t}] being non-decreasing and [X] being bounded in Assumption [reference].

Substituting ([reference])-([reference]) into the RHS of ([reference]) and rearranging terms, we have
[Equation]

For the last two terms on the RHS of ([reference]), completing the square, we have
[Equation]
where [(a)] follows from the bound on [f_t(x)] in Assumption [reference].

Substituting ([reference]) into ([reference]) yields ([reference]).[]

## Proof of Theorem~\ref{thm:reg

}

*Proof:* Summing ([reference]) over [t=2,,T] and noting that [Q_{t-1}^{n}[g_{t-1}^{n}(x_t)]_+0,t>1,n], we have
[Equation]
where [(a)] follows from [X] being bounded in Assumption [reference].

Also, for any [t], we have
[Equation]
where [(a)] follows from the convexity of [f_t(x)], [(b)] is due to the fact that [,b], and [(c)] follows from [X] and [f_t(x)] being bounded in Assumptions [reference] and [reference] , respectively.

Combining ([reference]) and [f_T(x_T)-f_T(x_T^)DR] from ([reference]), we complete the proof. []

## Proof of Theorem~\ref{thm:vio

}

*Proof:* Substituting the upper bound on the Lyapunov drift in ([reference])
of Lemma [reference] into the per-slot performance bound of COLDQ in ([reference]) of Lemma [reference] and
rearranging terms, we have
[Equation]

Dividing both sides of ([reference]) by [] and summing over
[t=2,,T], we have
[Equation]

We now bound the RHS of ([reference]). We have
[Equation]
which follows from the bound on [X] in Assumption [reference].

Also, we have
[Equation]
which follows from ([reference]) in the proof of Theorem [reference].

We can show that
[Equation]
where [(a)] follows from the definition of [_{t-1}] in ([reference]), and [(b)] is because [Q_1^n=,n] by initialization.

Substituting ([reference])-([reference]) into ([reference]), we have
[Equation]

Further noting that [[g_1^n(x_1)]_+|g_1^n(x_1)|G,n] from Assumption [reference], we complete the proof.[]

## Proof of Theorem~\ref{thm:strong

}

*Proof:* Replacing the dynamic benchmark [{x_t^}] with the offline benchmark [x^] in ([reference]) of the proof of Lemma [reference], we have
[Equation]

We now bound the RHS of ([reference]). From the []-strongly convexity of [f_{t-1}(x)], the first term on the RHS of ([reference]) can be upper bounded as
[Equation]

From the definition of the offline benchmark [x^],
the second term on the RHS of ([reference]) satisfies
[Equation]

Substituting ([reference]) and ([reference]) into the RHS of ([reference]) and rearranging terms, we have
[Equation]
where [(a)] follows from [Q_{t-1}^n[g_{t-1}^n(x_t)]_+0,n] and ([reference]) in the proof of Lemma [reference].

Summing ([reference]) over [t=2,,T], we have
[Equation]
where [(a)] follows from [X] being bounded in Assumption [reference].

Further noting that [f_T(x_T)-f_T(x^)DR] similar to the proof of ([reference]), we complete the proof.[]

## Proof of Corollary~\ref{cor:conv

}

*Proof:* Substituting [_t=t^1-V_x{2}] into the dynamic regret bound ([reference]) in Theorem [reference], we have
[Equation]
where [(a)] follows from Lemma [reference] and [(b)] is because [_{t=2}^T_t^-x_{t-1}^=O(T^{V_x})] in ([reference]).

Substituting [_t=t^1-V_x{2}], [=1{T}] and [=T]
into the hard constraint violation bound ([reference]) in Theorem [reference], we
have
[Equation]
where [(a)] follows from Lemma [reference] and [(b)] is because [_{t=2}^T_t^-x_{t-1}^=O(T^{V_x})]
in ([reference]) and [_{t=2}^T_{x}_t(x)-g_{t-1}(x)=O(T^{V_g})] in ([reference]).[]

## Proof of Corollary~\ref{cor:strong

}

*Proof:* Substituting [_t=t] into the static regret bound ([reference]) in Theorem [reference], we have
[Equation]

Substituting [_t=t], [=1{T}], and [=T] into ([reference]) in Theorem [reference] with the dynamic benchmark [{x_t^}] replaced by the offline benchmark [x^], we have
[Equation]
where [(a)] follows from [_{t=2}^T_{x}_t(x)-g_{t-1}(x)=O(T^{V_g})]
in ([reference]).[]

## COLDQ with Expert Tracking

We extend the basic COLDQ algorithm with expert tracking in Algorithm [reference], which can achieve the same performance bounds as COLDQ without the knowledge of [V_x] to set the algorithm parameter [_t]. The idea of expert tracking is to run multiple Algorithm [reference] in parallel, each tracks a different [V_x], and then aggregate the decisions of different experts. 

The expert-tracking algorithm in [citation] is for OCO with *short-term* constraints only, while the algorithm in [citation] is for OCO with *fixed* constraints. In contrast, Algorithm [reference] is the first *time-varying* constrained OCO algorithm to provide [O(T^1+V_x{2})] dynamic regret and [O(T^{V_g})] constraint violation that recover the best-known [O(T^1{2})] regret and [O(1)] violation, without any prior knowledge of the system dynamics.

[Algorithm]
algorithm

corollary[Expert Tracking]
	*Under Assumptions [reference]-[reference], for any [V_x[0,1]] and [V_g[0,1]], let [M=1*{2_2(1+T)+1]. [=T^{-1{2}}], [_t[m]=t^1{2}/2^{m-1}], [=T^{-3{2}}] and [=T^3{2}], where [(0,G)], COLDQ-Expert achieves:}
	[Equation]
corollary

## Proof of Corollary~\ref{cor:expert

}

*Proof:* We first derive the dynamic regret bound. Following the Proof of ([reference]) in Theorem [reference], we can show that for each [m]:
[Equation]
where [(a)] is because of setting [_t[m]=t^1{2}/2^{m-1}]and [(b)] follows from Lemma [reference].

Since the number of experts is set as [M=1{2}_2(1+T)+1], there exists an expert
[Equation]
such that
[Equation]

Substituting ([reference]) into ([reference]), we have
[Equation]

Also, we have
[Equation]
where [(a)] follows from the convexity of [f_t(x)], [(b)] is because [l_t(x)=_t(x_t),x-x_t], [(c)] follows from Lemma [reference] and [|l_t(x)|DR,,t] under Assumptions [reference] and [reference].

Recall [w_1[m]=M+1{m(m+1)M}] by initialization, we have
[Equation]

Substituting ([reference]) into ([reference]) and noting that [=T^{-1{2}}], we have
[Equation]

Combining ([reference]) and ([reference]), we have
[Equation]
where [(a)] follows from [_{t=2}^T_t^-x_{t-1}^=O(T^{V_x})]
in ([reference]).

We now derive the hard constraint violation bound. Replacing [{x_t}] with [{x_t[m]}] in the proof of Theorem [reference], for each expert [m], we can show that
[Equation]
where [(a)] follows from setting [_t[m]=t^1{2}/2^{m-1}], [=T^{-3{2}}], and [=T^3{2}], [(b)] is because [m1{2}_2(1+T)+1,m] and [_{t=1}^Tt^{-1{2}}2T^1{2}] from Lemma [reference], and [(c)] follows from [_{t=2}^T_t^-x_{t-1}^=O(T^{V_x})] in ([reference]) and [_{t=2}^T_{x}_t(x)-g_{t-1}(x)=O(T^{V_g})] in ([reference]).

Noting that [g_t^n(x),t,n] is convex and [x_t=_{m=1}^Mw_t[m]x_t[m]] with [_{m=1}^Mw_t[m]=1,t], We then have
[Equation]
where [(a)] follows from [x_t=_{m=1}^Mw_t[m]x_t[m],t], [(b)] is due to the convexity of [g_t^n(x),t,n], and [_{m=1}^Mw_t[m]=1,t], and [(c)] follows from [_{n=1}^N_{t=1}^T[g_t^n(x_t[m])]_+=O(T^{V_g}),m] in ([reference]). []

## Experiment Details

We provide all the algorithm parameters used in our experiments, the intuition behind the fine-tuning of all algorithms for fair comparison, and the detailed problem settings of the application to online job scheduling.

#### Experiment on Time-Varying Constraints.

In Table [reference], we summarize all algorithm parameters used to generate Figure [reference]. For fair comparison among COLDQ (this work), RECOO [citation], and Algorithm 1 [citation], we fine-tuned their suggested parameters such that they reach as close accumulated loss as possible at the end. In this way, we can focus on comparing the algorithm performance in terms of the hard constraint violation.

[Table]

#### Experiment on Fixed Constraints.

In Tables [reference] and [reference], we summarize all algorithm parameters used to generate Figures [reference] and [reference]. Similar to the previous experiment, we fine-tuned the suggested parameters of all algorithms to reach nearly the same accumulated loss, and compare their hard constraint violations.

[Table]

[Table]

#### Application to Online Job Scheduling.

We experiment on the practical online job schedulig problem considered in [citation]. This application aims at allocating power across data centers to minimize the energy cost subject to service quality constraints. We consider [100] data centers equally distributed in [10] regions. The duration of each time slot [t] is 5 minutes. Let [x_t=[x_t^1,,x_t^{100}]^^{100}] be the power allocation decision at time [t]. The loss function [f_t(x_t)] representing the energy cost is set as [f_t(x_t)=_t,x_t], where [c_t^{100}] is the time-varying electricity price vector. The constraint function [g_t(x_t)] representing the service quality is set as [g_t(x_t)=_t-_{i=1}^{100}h_i(x_t^i)], where [_t] is the job arrival rate and [h_i(x_t^i) = 4(1 + 4x_t^i)] models the service capacity of each data center. The constraint violation measures the amount of delayed jobs not finished in time. We use real-world electricity price data from NYISO (available from http://www.nyiso.com/.) for 10 New York City regions between [05/01/2017] and [05/10/2017]. The number of arriving jobs [_t] at each time [t] is generated from a Poisson distribution with mean [2500]. The feasible set [X] is set as [X={x_t|0x_t^i1000,t,i}].

In Table [reference], we summarize all algorithm parameters used to generate Figure [reference]. We fine-tuned the suggested parameters of COLD (this work) and RECOO [citation] to reach nearly the same number of average delayed jobs at the end. We optimized the suggested parameters of Algorithm 1 [citation] to reach its best performance.

[Table]

We implemented all algorithms in Python 3.8.19 with CVXPY 1.5.1. A laptop with Intel(R) Core(TM) i5-13600K CPU@3.50GHz and 32 GB of RAM can finish a single run of each algorithm within 10 ms per iteration.

