# Mighty-K–Clifford–Weil: a rigorous local audit and the operator obstruction

Research audit, 5 November 2026.

The arithmetic construction yields quantitative 3-adic equidistribution, exact finite Clifford realizations, and coefficientwise convergence to a local Euler factor. It does not presently yield a positive realization of the Weil form. Two explicit obstructions are proved below: the signed contribution of an individual prime is indefinite, and every natural finite-prime truncation retaining the exact pole and real-place terms is indefinite on the full test-function space.

All computations use integers and rational numbers. The accompanying files mighty_k_audit.py and mighty_k_exact_results.json contain the reproducible calculation and its output. The script uses subset dynamic programming through K=13 and checks it against direct enumeration through K=8.

## Deliverable 1. Verified theorem ledger

Put m=K-1. Throughout, “proved” means proved below from the stated definitions, not inferred from a numerical fit.

| Claim | Classification | Dependencies or correction |
|---|---|---|
| Integrality of Y and identity (1) | Proved from definitions | Expand the concatenation into place values. |
| Pair formula (2) | Proved; stronger modulo 9 | The identity ell_D congruent to D holds modulo 9. |
| A: A_(3q+1,1)=A_(3q,1) | Proved | Free cyclic action on 3q distinct blocks; complete triads have constant digit length. |
| The same period-three identity modulo 9 or 27 | False | K=3 versus K=4 gives different distributions already modulo 9. |
| Weaker depth-two identity A_(9q+1,2)=A_(9q,2) | Proved | The cyclic argument works modulo 9 on complete groups of nine. |
| Extending that weaker identity to depth three | False in general | K=9 versus K=10 have different probabilities of divisibility by 27. |
| Exact reversal formula (7) and congruence (8) | Proved | The addition formula for ell. |
| Reversal makes depth-one coefficients real for every K | Proved | Theta_K is always divisible by 3. |
| Reversal makes all depth-two coefficients ordinarily real | False | K=3, j=1 gives exp(i pi/3) cos(pi/9). |
| Depth-two phase-rotated reality | Proved | exp(-pi i j Theta_K/9) A_(K,2)(j) is real. |
| Adjacent-swap identity and primitive contraction | Proved | The sign convention is Y(ab)-Y(ba) in (9). |
| Independent averaging over disjoint adjacent pairs | Proved | Suffix digit totals do not depend on orientations. |
| Proposed bound (12) | Proved, and strengthened | For K>=3, primitive j: abs(A)<=exp(-(K-1)/(72*9^r)). |
| Total variation at growing depth | Proved | In fact 9^r=o(K-1) suffices; see the Fourier-sum estimate below. |
| Supplied depth-one regression table | Proved from definitions by exact finite computation | Every supplied value agrees with the integer DP. |
| Supplied lambda_5(1), lambda_6(1) | Proved from definitions by exact finite computation | 9/20 and 31/24. |
| Formula (20), as pasted | Missing a sign | The correct formula is 2c_2/c_0-(c_1/c_0)^2. |
| Nonnegativity of all finite-K logarithmic coefficients | False | lambda_5(2)=-81/400. |
| Coefficientwise c_n ->1 and lambda_n ->1 | Proved | Fixed-depth equidistribution. |
| Local analytic convergence | Proved on Re(s)>1 | Stronger domains need additional tail estimates. |
| Collision, Parseval, chi-square, and pointed bound | Proved | All normalizations (25)-(29) are correct. |
| Universal improvement of (29) from E alone | Impossible | Its constant is sharp; extra reversal symmetry can improve it. |
| Clifford realizations of the local functionals | Proved | An explicit exterior-algebra module is supplied. |
| Clifford positivity implies Weil positivity | Conjectural bridge, not established | No identity identifies either local Gram form with the signed global Weil form. |
| Orthogonal positive contributions equal to each signed prime term | False | A two-bump counterexample proves indefiniteness. |
| Natural finite-prime Weil truncations are positive | False | The separated odd-bump construction proves indefiniteness. |
| A non-circular factorization of the full Weil form | Conjectural | The unresolved operator inequality is specified in Deliverable 6. |
| Positivity of the full Weil form on all compactly supported smooth tests iff RH | Established theorem, with proof recalled below | All supports and all complex test functions are needed, or an appropriate determining subclass. |

### 1.1 Integer identity and a stronger reduction

For a permutation pi=(n_1,...,n_m),

\[
C_K(\pi)=\sum_i n_i10^{D_i},\qquad
Y_K(\pi)=\sum_i n_i\ell_{D_i}.
\]

The binomial expansion gives

\[
\ell_D=\sum_{h=1}^{D}9^{h-1}\binom Dh,\qquad
\ell_D\equiv D\pmod9.
\]

Thus the supplied congruence (2) actually holds modulo 9:

\[
Y_K(\pi)\equiv \sum_{i<k}n_i d(n_k)\pmod9.
\tag{A1}
\]

### 1.2 Complete proof of the period-three identity

Take m=3q and let the cyclic group C_m rotate the m positions. The action is free: a nonidentity rotation cannot fix a list of distinct labels. Every orbit therefore has exactly m elements.

Write S=sum n and D=sum d(n) over 1,...,m. Moving the first block a to the end changes the right side of (A1) by

\[
d(a)(S-a)-a(D-d(a))=d(a)S-aD.
\]

Both S and D vanish modulo 3. For D this follows by splitting 1,...,3q into consecutive triads; a decimal boundary is 10^h congruent to 1 modulo 3, so it is always the first member of a triad. Hence every rotation preserves Y modulo 3.

Each orbit has a unique representative (3q,sigma). Its residue is

\[
3q\sum_{n<3q}d(n)+Y_{3q}(\sigma)
\equiv Y_{3q}(\sigma)\pmod3.
\]

There is one such representative for each sigma in S_(3q-1). If c_a(K) denotes the number of permutations with residue a, then

\[
c_a(3q+1)=3q\,c_a(3q).
\]

Dividing by (3q)! proves the Fourier identity for every integer j.

Exactly the same proof modulo 9 works when m=9q, because powers of ten are 1 modulo 9 and each complete group of nine has constant digit length:

\[
A_{9q+1,2}(j)=A_{9q,2}(j).
\tag{A2}
\]

The originally proposed period three does not extend to depth two. For K=3 the Y-values are 1,2. For K=4 they are 13,14,23,25,34,35, with residues 4,5,5,7,7,8 modulo 9. Failure modulo 9 also rules out equality of their full distributions modulo 27.

Even (A2) does not automatically extend to depth three:

\[
\Pr(27\mid Y_9)=\frac{1491}{40320},\qquad
\Pr(27\mid Y_{10})=\frac{13026}{362880}.
\]

The latter numerator would have to be 9*1491=13419 for equality.

### 1.3 Reversal, including its exact phase

For each position, P_i+D_i=D(K)-d(n_i). Consequently

\[
\Theta_K
=\sum_i n_i(\ell_{P_i}+\ell_{D_i}+9\ell_{P_i}\ell_{D_i}),
\]

which proves the exact reversal formula.

There is a short closed answer for Theta modulo 9. Let h=d(m). Every completed decimal tier has both its size and the sum of its labels divisible by 9. Therefore

\[
D(K)\equiv hm,\qquad
\sum_{n=1}^m n d(n)\equiv h\frac{m(m+1)}2\pmod9,
\]

and hence

\[
\boxed{\Theta_K\equiv h\,\frac{m(m-1)(m+1)}2\pmod9.}
\tag{B1}
\]

Division by 2 here is ordinary integer division; equivalently use the inverse of 2 modulo 9. The cubic factor modulo 9, for m=0,...,8 modulo 9, is

\[
0,0,3,3,3,6,6,6,0.
\]

In particular Theta_K=0 modulo 3 for every K, which proves ordinary reality at depth one, not merely a phase-rotated statement.

For r<=2,

\[
A_{K,r}(j)=e^{2\pi i j\Theta_K/3^r}\overline{A_{K,r}(j)}.
\tag{B2}
\]

Thus exp(-pi i j Theta_K/3^r) A is real. At depth two it need not itself be real; K=3 gives the explicit nonreal value in the ledger.

At every depth the exact correction is

\[
Y(\pi)+Y(\pi^{\rm rev})
\equiv\Theta_K-9H(\pi)\pmod{3^r},\qquad
H(\pi)=\sum_i n_i\ell_{P_i}\ell_{D_i}.
\tag{B3}
\]

Modulo 27 and modulo 81 the correction is -9 sum_i n_i P_iD_i. More generally expand

\[
9H=
\sum_{a,b\ge1}3^{2(a+b-1)}
\sum_i n_i\binom{P_i}{a}\binom{D_i}{b},
\]

retaining exactly the terms with 2(a+b-1)<r.

The first possible nonzero correction is depth three. For K=4 and pi=(1,2,3), Theta=66 and H=2, while Y(pi)+Y(pi^rev)=13+35=48. Their difference is 18, nonzero modulo 27. At greater depth (B2) is replaced by

\[
A_{K,r}(j)=e^{2\pi i j\Theta_K/3^r}
\mathbb E\!\left[e^{-2\pi i jY/3^r}e^{-2\pi i j9H/3^r}\right].
\]

The second factor cannot in general be removed from the expectation.

## Deliverable 2. Exact arithmetic

### 2.1 The recurrence and independent checks

For a subset S of blocks define D(S)=sum_(n in S)d(n). Let v_S(a) count the orderings of S whose centered value is a modulo M. Start with v_empty(0)=1. Prepending n not in S gives

\[
v_{S\cup\{n\}}\bigl(a+n\ell_{D(S)}\bmod M\bigr)
\mathrel{+}=v_S(a).
\tag{DP}
\]

This is exact integer arithmetic and costs O(M m 2^m) operations. No complex floating point or reconstruction of rationals is involved. Direct enumeration through K=8 independently reproduces these distributions and checks the exact reversal and swap identities for every tested permutation.

For depth one, if counts are (c_0,c_1,c_2), reversal proves c_1=c_2 and

\[
A_{K,1}(1)=\frac{2c_0-c_1-c_2}{2m!}.
\]

| K | c_0 | c_1=c_2 | A_(K,1)(1) |
|---:|---:|---:|---:|
| 3 | 0 | 1 | -1/2 |
| 4 | 0 | 3 | -1/2 |
| 5 | 4 | 10 | -1/4 |
| 6 | 48 | 36 | 1/10 |
| 7 | 288 | 216 | 1/10 |
| 8 | 1824 | 1608 | 3/70 |
| 9 | 13104 | 13608 | -1/80 |
| 10 | 117936 | 122472 | -1/80 |
| 11 | 1197504 | 1215648 | -1/200 |
| 12 | 13448592 | 13234104 | 331/61600 |
| 13 | 161383104 | 158809248 | 331/61600 |

There is no discrepancy in the supplied regression data.

### 2.2 Full depth-two distributions and collision traces

Each row below consists of counts, divided by N to obtain probabilities.

| K | N | Counts for residues 0,1,...,8 | Theta mod 9 | C_(K,2) | E_(K,2) |
|---:|---:|---|---:|---:|---:|
| 4 | 6 | (0,0,0,0,1,2,0,2,1) | 3 | 5/18 | 3/2 |
| 5 | 24 | (1,4,4,1,4,2,2,2,4) | 3 | 13/96 | 7/32 |
| 6 | 120 | (17,12,14,14,14,12,17,10,10) | 6 | 827/7200 | 27/800 |

Every row satisfies count(a)=count(Theta-a modulo 9). The collision trace is sum count(a)^2/N^2 and E=9C-1.

### 2.3 Shell counts and logarithmic derivatives

Let t_n be the number of permutations with v_3(Y)=n. Counts modulo 27 determine t_0,t_1,t_2 exactly. Higher valuations are not mistakenly assigned to t_2.

| K | (t_0,t_1,t_2) | lambda_(K,3)(1) | lambda_(K,3)(2) |
|---:|---|---:|---:|
| 3 | (2,0,0) | 0 | 0 |
| 4 | (6,0,0) | 0 | 0 |
| 5 | (20,3,0) | 9/20 | -81/400 |
| 6 | (72,31,10) | 31/24 | 479/576 |
| 7 | (432,194,63) | 97/72 | 4199/5184 |
| 8 | (3216,1218,401) | 609/536 | 273927/287296 |
| 9 | (27216,8730,2883) | 485/504 | 249119/254016 |
| 10 | (244944,78570,26340) | 485/504 | 28495/28224 |

For K=5 the entire valuation histogram is t_0=20,t_1=3,t_3=1; all other entries vanish. The exceptional permutation is (3,4,1,2), with Y=378=14*27. Thus

\[
Z_{5,3}(z)=\frac54+\frac9{16}z+\frac{27}{16}z^3,\qquad
\widetilde Z_{5,3}(z)=1+\frac9{20}z+\frac{27}{20}z^3.
\]

For K=6 the entire histogram is (72,31,10,5,1,1), and

\[
(c_0,c_1,c_2)=\left(\frac9{10},\frac{93}{80},\frac98\right).
\]

The correct second logarithmic coefficient has a minus sign:

\[
\lambda_2=2\frac{c_2}{c_0}-\left(\frac{c_1}{c_0}\right)^2.
\]

This explains both listed values and proves that the finite logarithmic coefficients are not automatically positive spectral weights.

### 2.4 Zero values, actual local integrals, and convergence

For K=2, Y=0 for the only permutation. Its valuation is infinity. All finite shell coefficients vanish, Z_(2,3)=0, and normalization by c_0 and the logarithmic derivative are undefined.

For K>=3, every permutation has at least two blocks; the first term n_1 ell_(D_1) is strictly positive and all terms are nonnegative. Hence Y>0. Also c_0>0: place 1 and 2 adjacently and compare the two orientations, whose Y-values differ by a 3-adic unit. They cannot both be divisible by 3. Its finite set of values gives a finite maximum valuation. Z_(K,3)(z) is a polynomial and Z_(K,3)(s) is entire. Its logarithmic derivative is meromorphic, with poles at zeros of that polynomial after substitution z=3^(-s). The logarithmic power series is initially a formal series, or an analytic series up to the nearest zero.

Normalize additive Haar measure dx on Z_3 to have mass 1, and multiplicative Haar measure d^*x on Q_3^* to give Z_3^* mass 1. Each multiplicative shell has measure 1 and its additive measure is (2/3)3^(-n). Define a radial function phi_K by phi_K(x)=c_(K,3)(n) when v_3(x)=n>=0, and zero otherwise. For K>=3 this is a compactly supported locally constant function, including at zero after setting phi_K(0)=0. Then

\[
\int_{\mathbb Q_3^\times}\phi_K(x)|x|_3^s\,d^*x
=\sum_{n\ge0}c_{K,3}(n)3^{-ns}.
\]

Thus the normalization is exactly a radial additive-density normalization, followed by a multiplicative Tate integral. An atom at zero is not represented by any finite shell; K=2 must remain separate.

Write L_r=Pr(3^r divides Y), L_0=1. For every finite n,

\[
P(v_3(Y)=n)=L_n-L_{n+1},\qquad
c_n=\frac32\,3^n(L_n-L_{n+1}).
\tag{D1}
\]

Fixed-depth equidistribution gives L_r ->3^(-r), so c_n ->1 for each n. For b_n=c_n/c_0, b_0=1, the formal identity z Z'=Z sum lambda_m z^m gives

\[
\lambda_m=mb_m-\sum_{k=1}^{m-1}\lambda_k b_{m-k}.
\tag{D2}
\]

Induction proves lambda_m ->1. Convergence of the residue law modulo 3^(m+1) suffices for this particular coefficient; weak convergence on Z_3 supplies it for every fixed m.

Analytic convergence is a separate statement. Since

\[
0\le c_n\le\frac32\,3^n,
\]

the polynomials converge locally uniformly, with all derivatives, on |z|<1/3 to (1-z)^(-1). The limit is nonzero there, so the normalized logarithmic derivatives also converge locally uniformly on this disk, equivalently on Re(s)>1.

There is a modest extra statement for Z itself: convergence is uniform on |z|<=1/3. Indeed the tail there is bounded by (3/2)Pr(v_3(Y)>=R), whose limsup is (3/2)3^(-R). This does not give convergence of derivatives on the boundary. For every K>=3, Z_(K,3)(1/3)=3/2 exactly.

No convergence on the whole disk |z|<1, or on all Re(s)>0, follows merely from fixed-depth equidistribution. Small mass epsilon_K at valuation n_K tending to infinity can preserve every fixed residue limit while contributing (3/2)epsilon_K*3^(n_K(1-s)). Additional uniform exponential-moment estimates are needed to rule this out for the actual permutation measures.

For Haar measure, the integral is (1-p^(-s))^(-1), and its negative logarithmic derivative is

\[
(\log p)\sum_{a\ge1}p^{-as}.
\]

This is exactly the von Mangoldt prime-power coefficient. It is an Euler-factor calculation, not a positivity theorem. A global prime sum is absolutely convergent in Re(s)>1; coefficientwise local convergence alone does not justify a limiting sum over all primes.

## Deliverable 3. Quantitative adjacent-swap theorem

The following estimates are unconditional. The constants are conservative; an exact finite-m mean is retained for sharper applications.

### 3.1 Factorization

Pair the positions (1,2),(3,4),..., leaving the last position unpaired if needed. Condition on the ordered collection of unordered pairs and the leftover label. Their orientations are independent fair bits.

The total digit length of every pair is orientation-independent. Thus the suffix length after a pair is fixed under every orientation change, including changes in later pairs. Relative to a fixed orientation,

\[
Y=y_0+\sum_{a=1}^{\lfloor m/2\rfloor}\epsilon_a\Delta_a,
\qquad
\Delta_a=10^{\ell_a}
\bigl(u_a\ell_{d(v_a)}-v_a\ell_{d(u_a)}\bigr).
\]

The orientation average therefore has modulus

\[
\prod_a\left|\frac{1+e^{2\pi i j\Delta_a/M}}2\right|
=\prod_a|\cos(\pi j\Delta_a/M)|.
\tag{C1}
\]

For an active pair, Delta_a is a unit modulo 3 and hence modulo M=3^r. If j is primitive modulo M, j Delta_a is a nonzero unit, so each such factor is at most cos(pi/M). Denote the number of active pairs by H.

### 3.2 Exact active-pair mean and a uniform lower bound

Let n_(a,b) count labels with (n mod 3,d(n) mod 3)=(a,b). The number of active unordered edges among all labels is

\[
e_m=\frac12\sum_{\substack{a,b,c,d\in\mathbb F_3\\ad-cb\ne0}}
n_{a,b}n_{c,d}.
\]

Consequently

\[
\mu_m:=\mathbb EH=
\lfloor m/2\rfloor\,\frac{e_m}{\binom m2}.
\tag{C2}
\]

Here is a uniform bound sufficient for every conclusion:

\[
\boxed{\mu_m\ge m/18\qquad(m\ge2).}
\tag{C3}
\]

Proof. Let H_good(t) count labels <=t whose digit length is not divisible by 3. In each group of three successive decimal tiers, the first two tiers are good and the third is bad. The ratio H_good(t)/t increases through a good portion and decreases through a bad portion. At t=1000^a-1 it is exactly 99/999=11/111. Hence H_good(t)>=11t/111 for all t.

Put m_0=3 floor(m/3). On 1,...,m_0, the three label residues occur equally often within each digit-length class. If u counts labels whose digit length is 0 modulo 3, an elementary count of determinants over F_3 gives

\[
e_{m_0}=\frac13(m_0^2-u^2)
\ge\frac{2321}{36963}m_0^2>\frac1{16}m_0^2.
\]

Since 2 floor(m/2)>=m-1, (C2) implies mu_m>=e_m/m. Thus for m>=36,

\[
\mu_m\ge\frac{(m-2)^2}{16m}
\ge\frac{289}{5184}m>\frac m{18}.
\]

For 3<=m<=35, all digit lengths are 1 or 2. Pair any label divisible by 3 with any label not divisible by 3; all these edges are active. There are at least (m/5)(2m/3) such edges, giving mu_m>=2m/15. The case m=2 has H=1. This proves (C3).

### 3.3 Concentration with explicit constants

Generate the pairing by a uniform random permutation and expose that permutation one entry at a time. Transposing two entries changes at most two pair indicators, so changes H by at most 2.

Conditioned on a prefix, two possible next labels can be coupled by exchanging those labels in the unexposed positions. Their conditional expectations differ by at most 2. Each martingale difference therefore has a conditional range of length at most 2. Hoeffding's lemma, iterated over at most m exposures, gives

\[
\mathbb E e^{t(H-\mu_m)}\le e^{mt^2/2},\qquad
\Pr(H\le\mu_m-u)\le e^{-u^2/(2m)}.
\tag{C4}
\]

This is a complete bounded-difference proof; independence of the pair indicators is neither asserted nor needed.

### 3.4 Fourier bounds

Set beta_r=-log cos(pi/3^r) and q=min(beta_r,mu_m/m). From (C1), H>=0, and (C4),

\[
\boxed{
|A_{K,r}(j)|
\le\mathbb E e^{-\beta_r H}
\le \exp(-q\mu_m+mq^2/2)
}
\tag{C5}
\]

for primitive j. This exact-mean estimate is preferable to the uniform constants when computing specific K.

Since beta_r>=pi^2/(2*9^r) and mu_m>=m/18, it follows that

\[
\boxed{|A_{K,r}(j)|\le e^{-m/(72\,9^r)}.}
\tag{C6}
\]

Indeed if q=mu_m/m, the exponent is at most -m/648, which is no larger than -m/(72M^2) for M>=3. If q=beta_r, the exponent is at most -mu_m beta_r/2 <=-pi^2 m/(72M^2).

A nonzero character of conductor 3^s has A_(K,r)(j)=A_(K,s)(j/3^(r-s)), so the same result applies with s in place of r. There is no depth-independent gap.

### 3.5 A Fourier-sum estimate avoiding the square-root-M loss

Using (C6) alone and Parseval gives

\[
E_{K,r}\le(M-1)e^{-m/(36M^2)},\qquad
\|\mu_{K,r}-U_M\|_{\rm TV}\le\frac12\sqrt{E_{K,r}}.
\]

A stronger argument is available. Jensen applied to the conditional characteristic function, followed by Holder over the active pairs, gives

\[
E_{K,r}
\le\mathbb E\sum_{j=1}^{M-1}
\prod_{a=1}^H\cos^2(\pi j\Delta_a/M)
\le\mathbb E\sum_{j=1}^{M-1}|\cos(\pi j/M)|^{2H}.
\tag{C7}
\]

For the Holder step, multiplication by each unit Delta_a permutes the nonzero residues modulo M, so all Holder factors have the same sum. If H=0 the sum is M-1, interpreted separately.

On H>=mu_m/2, pair j with M-j and use cos x<=exp(-x^2/2) for 0<=x<=pi/2. Combining with (C4) yields

\[
E_{K,r}\le
(M-1)e^{-\mu_m^2/(8m)}
+2\sum_{j\ge1}\exp\!\left(-\frac{\pi^2\mu_m}{2M^2}j^2\right).
\tag{C8}
\]

In particular, with x=pi^2 m/(36M^2),

\[
\boxed{
E_{K,r}\le
(M-1)e^{-m/2592}
+\frac{2e^{-x}}{1-e^{-3x}},
\qquad
\|\mu_{K,r}-U_M\|_{\rm TV}\le\tfrac12\sqrt{E_{K,r}}.
}
\tag{C9}
\]

The geometric estimate uses j^2>=1+3(j-1). Therefore

\[
\boxed{9^{r(K)}=o(K-1)\quad\Longrightarrow\quad
\|\mu_{K,r(K)}-U_{3^{r(K)}}\|_{\rm TV}\longrightarrow0.}
\tag{C10}
\]

This includes r<=(1/2-epsilon)log_3(K-1), and more generally
r=(1/2)log_3(K-1)-omega(1). No optimality beyond this range is claimed.

## Deliverable 4. Finite Clifford construction and sharp local errors

### 4.1 Ordinary Hilbert-space construction first

Let W=C^N have orthonormal basis e_pi and V=C^M have orthonormal basis e_a. Define

\[
Be_\pi=e_{Y(\pi)\bmod M},\qquad
R=\frac1NBB^*.
\]

Then B^*B=G and R=diag(mu(0),...,mu(M-1)). Consequently

\[
\frac{\operatorname{Tr}G^2}{N^2}
=\operatorname{Tr}R^2=\sum_a\mu(a)^2.
\]

The unitary finite Fourier transform sends the vector (mu(a)) to (A(j)/sqrt M), so

\[
\mathcal C=\frac1M\sum_j|A(j)|^2,\qquad
E=M\|R-I_V/M\|_{\rm HS}^2=\sum_{j\ne0}|A(j)|^2.
\tag{E1}
\]

Also

\[
L=\langle e_0,Re_0\rangle
=\frac1M\sum_j A(j).
\]

These prove (25)-(28), including the chi-square normalization.

For delta_a=mu(a)-1/M, sum delta_a=0. Thus

\[
|\delta_0|^2
\le \frac{M-1}{M}\sum_a|\delta_a|^2
=\frac{M-1}{M^2}E.
\tag{E2}
\]

Equality is attained when all delta_a for a!=0 are equal, for every sufficiently small positive or negative delta_0. Hence no smaller universal constant follows from E alone. The naive residue-space bound E/M is weaker; projecting away the constant vector gives exactly (E2), the Fourier Cauchy-Schwarz constant.

Probability constraints also give -1/M<=delta_0<=1-1/M. If an additional symmetry forces delta_0 to be shared by an orbit of t residues, the sharp linear-space bound improves to

\[
|\delta_0|^2\le\frac{M-t}{tM^2}E.
\]

At depth two, reversal gives t=2 whenever Theta_K is 3 or 6 modulo 9.

### 4.2 Explicit Clifford module

Let S=Lambda^* V with its standard Hermitian exterior-algebra inner product and vacuum Omega=1. Creation a_a^* is wedge multiplication by e_a and annihilation a_a is its adjoint. They satisfy the canonical anticommutation relations. The self-adjoint generators

\[
\gamma_{2a}=a_a^*+a_a,\qquad
\gamma_{2a+1}=i(a_a^*-a_a)
\]

satisfy gamma_i gamma_j+gamma_j gamma_i=2 delta_ij. Hence S is a complex Clifford module for Cl_(2M).

Define normalized states

\[
q_\pi=a^*_{Y(\pi)\bmod M}\Omega.
\]

Their Gram matrix is G. Regard R=(1/N)sum_pi |q_pi><q_pi| as acting on S, zero off the one-particle subspace. Let P_0=|e_0><e_0| and I_1 be the projection onto that subspace.

For complete explicitness, the vacuum projection is

\[
\Pi_\Omega=\prod_a(1-a_a^*a_a),
\]

and the one-particle matrix units are a_a^* Pi_Omega a_b. Thus R, P_0, and I_1 are represented by Clifford elements, not merely abstractly added operators.

On H_Cl=End(S) with Hilbert-Schmidt inner product, left multiplication by a Clifford generator is self-adjoint. This is another explicit Clifford module. Its state vectors give

\[
\boxed{
\mathcal C=\langle R,R\rangle_{\rm HS},\qquad
L=\langle R,P_0\rangle_{\rm HS},\qquad
E=M\langle R-I_1/M,R-I_1/M\rangle_{\rm HS}.
}
\tag{E3}
\]

The pointed functional is linear in R; the collision functional is quadratic. All adjoints and reference vectors have now been specified.

No Clifford-specific theorem was needed. The construction embeds finite Gram positivity and Parseval into a Clifford module; it does not add a relationship to zeta zeros.

### 4.3 Optimal shell error from a single excess trace

At depth n+1, M=3^(n+1), the shell v_3(Y)=n consists of precisely the two residues 3^n and 2*3^n. Since c_n=(M/2)mu(shell), zero-sum Cauchy-Schwarz gives the sharp bound

\[
\boxed{|c_n-1|\le\sqrt{\frac{3^{n+1}-2}{2}\,E_{K,n+1}}.}
\tag{E4}
\]

It is sharp among arbitrary probability laws with a specified E, at least for sufficiently small deviations: take the deviation constant on the two-point shell and constant on its complement.

If two consecutive excesses are known, conductor orthogonality improves the available information. Set E_(K,0)=0. Then

\[
|c_n-1|\le
\sqrt{(3^n-1)E_{K,n}}
+\sqrt{\frac{3^n}{2}\bigl(E_{K,n+1}-E_{K,n}\bigr)}.
\tag{E5}
\]

Indeed, if S_n is the sum of all nontrivial Fourier coefficients at depth n and H_(n+1) the sum of primitive coefficients at depth n+1, then c_n-1=S_n-H_(n+1)/2. Their squared coefficient masses are E_n and E_(n+1)-E_n. Bounds using every conductor separately can be sharpened further by summing sqrt(2*3^(s-1)(E_s-E_(s-1))) for the corresponding conductor sums.

For e_n bounding |c_n-1| and e_0<1, set d_n=(e_n+e_0)/(1-e_0). Then |b_n-1|<=d_n, and in particular

\[
|\lambda_1-1|\le d_1,\qquad
|\lambda_2-1|\le2d_2+2d_1+d_1^2.
\]

An explicit bound for any fixed order follows recursively from (D2).

### 4.4 What can remain after renormalization?

For fixed r, (C6) gives exponential decay of E. Thus every polynomial renormalization K^a E_(K,r) tends to zero.

At depth one, the exact period-three identity gives E_(3q+1,1)=E_(3q,1). Therefore a renormalization a_K E_(K,1) can converge to a finite nonzero limit only if a_(3q+1)/a_(3q)->1. In particular no renormalization exp(alpha K)K^beta with alpha!=0 has a finite nonzero full-sequence limit. Grouped subsequences or more intricate normalizations are not excluded.

Self-normalization is possible but carries no new global information. At depth one

\[
\mu-U_3=\frac{A_{K,1}(1)}3(2,-1,-1).
\]

Where E is nonzero, the normalized rank-one outer product is the fixed projection onto (2,-1,-1)/sqrt6. Calling this a Weil form would be an unsupported identification.

There is also an information loss: translating a residue distribution preserves every |A(j)| and E but usually changes its mass at zero and its Tate shell coefficients. Collision traces alone cannot reconstruct pointed local arithmetic.

## Deliverable 5. The actual Weil form and the global operator analysis

### 5.1 Conventions

Use the complex test space D=C_c^infinity(R_+^*) with its usual LF topology. Define

\[
(f*g)(x)=\int_0^\infty f(y)g(x/y)\frac{dy}{y},
\qquad f^*(x)=\overline{f(x^{-1})},
\]

and the centered Mellin transform

\[
\mathcal Mf(s)=\int_0^\infty f(x)x^{s-1/2}\frac{dx}{x}.
\tag{W1}
\]

Then

\[
\mathcal M(f*g)=\mathcal Mf\,\mathcal Mg,\qquad
\mathcal M(g^*)(s)=\overline{\mathcal Mg(1-\bar s)}.
\]

For F=f*g^*, put h(u)=f(e^u), k(u)=g(e^u), and

\[
\widehat h(t)=\int_{\mathbb R}h(u)e^{itu}\,du.
\]

In particular MF(1/2+it)=hat h(t) overline(hat k(t)). The sesquilinear convention is linear in f and conjugate-linear in g.

Let psi=Gamma'/Gamma and define the real even symbol

\[
\Omega(t)=\Re\psi(1/4+it/2)-\log\pi.
\tag{W2}
\]

The exact Weil form in these conventions is

\[
\boxed{
Q_W(f,g)=P(f,g)
+\frac1{2\pi}\int_{\mathbb R}
\Omega(t)\widehat h(t)\overline{\widehat k(t)}\,dt
-\sum_p\sum_{a\ge1}\frac{\log p}{p^{a/2}}
\left[F(p^a)+F(p^{-a})\right],
}
\tag{W3}
\]

where

\[
P(f,g)=
\mathcal Mf(0)\overline{\mathcal Mg(1)}
+\mathcal Mf(1)\overline{\mathcal Mg(0)}.
\tag{W4}
\]

Thus in the benchmark's notation W_infinity is the negative of the Omega integral. It is important not to reverse this sign.

An equivalent spatial formula, with F(1) denoting its value at the identity, is

\[
\begin{aligned}
W_\infty(F)
={}&(\log(4\pi)+\gamma)F(1)\\
&+\int_0^\infty
\frac{e^{-u/2}\bigl[F(e^u)+F(e^{-u})\bigr]
-2e^{-u}F(1)}
{1-e^{-2u}}\,du.
\end{aligned}
\tag{W5}
\]

The numerator is O(u) at zero and the tail is integrable. No unmentioned principal-value prescription is needed for these tests.

### 5.2 Derivation of the signs and real-place normalization

Use the meromorphic completed function

\[
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

It has poles at 0 and 1, its other zeros are the nontrivial zeta zeros, and Lambda(s)=Lambda(1-s). Write H(s)=MF(s). A contour shift from c>1 to 1-c gives

\[
\sum_\rho H(\rho)-H(0)-H(1)
=\frac1{2\pi i}\int_{(c)}
\frac{\Lambda'}{\Lambda}(s)\,[H(s)+H(1-s)]\,ds.
\tag{W6}
\]

The sums count multiplicities. Compact smooth tests give rapid vertical decay, uniformly in bounded vertical strips. The classical zero-count bound O(T log T) makes the zero sum absolutely convergent, and the contour can be taken through heights avoiding zeros.

On the right line,

\[
\frac{\zeta'}{\zeta}(s)=-\sum_{n\ge2}\Lambda_{\rm vM}(n)n^{-s}.
\]

Mellin inversion sends H(s) to n^(-1/2)F(n) and H(1-s) to n^(-1/2)F(1/n). This gives the negative prime-power term in (W3).

For the gamma factor,

\[
\frac d{ds}\log\bigl(\pi^{-s/2}\Gamma(s/2)\bigr)
=-\tfrac12\log\pi+\tfrac12\psi(s/2).
\]

Its contour can be moved to Re(s)=1/2 without crossing a pole. Pairing t with -t produces exactly Omega(t), and hence the plus sign in front of the integral in (W3).

Finally, the digamma identity

\[
\psi(z)+\gamma
=\int_0^\infty\frac{e^{-v}-e^{-zv}}{1-e^{-v}}\,dv
\qquad(\Re z>0)
\]

and v=2u give (W5). The constant 2 log 2 needed to replace e^(-2u) by e^(-u) in the subtraction combines log pi+gamma into log(4pi)+gamma. This identity is also tabulated in NIST DLMF, equation 5.9.16.

These calculations yield the spectral identity, without RH,

\[
Q_W(f,g)=\sum_\rho
\mathcal Mf(\rho)\overline{\mathcal Mg(1-\bar\rho)}.
\tag{W7}
\]

The references at the end provide independent checks of the explicit formula and Weil criterion; all changes to the centered normalization have been displayed here.

### 5.3 Exact local translation operators: the weights can be produced, but the sign remains

On L^2(R,du), let U_a h(u)=h(u-a). For each prime p define the bounded self-adjoint operator

\[
B_p=(\log p)\sum_{a\ge1}p^{-a/2}
\bigl(U_{a\log p}+U_{-a\log p}\bigr).
\tag{W8}
\]

The series converges in operator norm, with

\[
\|B_p\|\le\frac{2\log p}{\sqrt p-1}.
\]

Equivalently, for V_p=p^(-1/2)U_(log p),

\[
B_p=(\log p)
\left[V_p(I-V_p)^{-1}+V_p^*(I-V_p^*)^{-1}\right].
\]

Its matrix coefficients give exactly W_p(f*g^*). The prime-power weights arise as the coefficients of the geometric resolvent, or equivalently from the logarithmic derivative of the Haar Tate factor at the centered Mellin parameter.

This construction is independent of RH. It also makes the obstruction explicit: the multiplier is

\[
b_p(t)=2\log p\,
\Re\frac{p^{-1/2+it}}{1-p^{-1/2+it}},
\]

with

\[
b_p(0)=\frac{2\log p}{\sqrt p-1}>0,\qquad
b_p(\pi/\log p)=-\frac{2\log p}{\sqrt p+1}<0.
\]

The weights are canonical once the local norm, its logarithm, and the half-density shift have been supplied. The collision module by itself does not supply a representation of the real translation group, this half-density normalization, or cross-place relations.

### 5.4 First concrete obstruction: an individual signed prime term is not a norm square

Fix p and a=log p. Choose a nonzero real phi in C_c^infinity(R) with support diameter less than a/2. Put

\[
h_+=\phi+U_a\phi,\qquad h_-=\phi-U_a\phi.
\]

The autocorrelations of phi at nonzero integer multiples of a vanish. A direct calculation gives

\[
W_p(h_+*h_+^*)=
2\frac{\log p}{\sqrt p}\|\phi\|_2^2,\qquad
W_p(h_-*h_-^*)=
-2\frac{\log p}{\sqrt p}\|\phi\|_2^2.
\tag{O1}
\]

Therefore neither W_p nor -W_p is positive semidefinite. In particular, there is no Hilbert map T_p with

\[
\|T_p f\|^2=-W_p(f*f^*)\quad\hbox{for every }f.
\]

This disproves any construction that tries to obtain the required negative prime terms as independent, orthogonal positive local contributions. It does not disprove a coupled global factorization with nontrivial cross terms.

The pole contribution is also indefinite. For instance a real odd log test has opposite centered Mellin values at 0 and 1, and P(f,f) is negative.

### 5.5 Stronger obstruction: every natural finite-prime truncation is indefinite

Let S be any fixed finite set of primes. Keep the exact pole and gamma terms and define

\[
q_S(h)=P(h,h)+
\frac1{2\pi}\int\Omega(t)|\widehat h(t)|^2dt
-\sum_{p\in S}\langle B_ph,h\rangle.
\tag{O2}
\]

The same argument applies if the powers at each prime are also truncated.

Choose a nonzero nonnegative even phi in C_c^infinity(R), and write

\[
I=\int_{\mathbb R}\phi(u)e^{u/2}du
=\int_{\mathbb R}\phi(u)e^{-u/2}du>0.
\]

For L exceeding the support radius, set h_L=U_L phi-U_(-L) phi. Then

\[
P(h_L,h_L)=-2I^2(e^{L/2}-e^{-L/2})^2.
\tag{O3}
\]

Meanwhile |hat h_L(t)|^2=4 sin^2(Lt)|hat phi(t)|^2, so the absolute value of its gamma contribution is bounded independently of L by

\[
\frac4{2\pi}\int|\Omega(t)|\,|\widehat\phi(t)|^2dt<\infty.
\]

Also ||h_L||_2^2=2||phi||_2^2 and every B_p is bounded. Thus the finite-prime sum is bounded independently of L. The negative pole term grows like -2I^2 e^L. Consequently

\[
\boxed{q_S(h_L)\longrightarrow-\infty.}
\tag{O4}
\]

This proves unconditionally that the natural finite-prime Weil truncations are not positive on D. They cannot be the Gram forms of the proposed T_(K,P,R).

A positive approximation would need a different construction: for example support-dependent compressions with proved positivity, or compensating terms that vanish on each fixed test while controlling tests whose supports escape. Neither property is supplied by local collision positivity.

### 5.6 The real place and global coupling

The real Gaussian gives the gamma factor directly:

\[
\int_{\mathbb R^\times}e^{-\pi x^2}|x|^s\frac{dx}{|x|}
=\pi^{-s/2}\Gamma(s/2),\qquad\Re s>0.
\]

Its logarithmic derivative supplies the operator symbol Omega. The global poles in (W6) arise from the completed zeta function; in the Tate-Poisson formulation they are tied to the zero orbit and the global summation formula. They are not obtained by adding more finite residue shells.

Thus an honest real-place component is available independently of RH, but it is a signed contribution. Equations (O1)-(O4) show why separately positive local modules cannot simply be added to it.

The first missing equality in the proposed route is an identification of a positive Gram form built from those modules with the full signed expression (W3). None of (E1)-(E5) supplies that equality. Defining a new Hilbert space by completing D in Q_W would assume the very positivity at issue.

### 5.7 Limits: what is and is not required

There is a useful simplification for this particular test class. If h and k have support in [-L,L], then F(e^u) has support in [-2L,2L]. Its prime-power contribution is a finite sum over p^a<=e^(2L). For each fixed test, one therefore does not need a prime-uniform estimate merely to pass a coefficient limit through that sum.

However, the result proved here is only at p=3. To replace all prime weights by permutation-generated coefficients, one still needs fixed-prime local theorems at every relevant p. For p not dividing 10, one must examine the corresponding swap units and digit-length classes. For p=2 and p=5, the suffix factor 10^ell is not a unit; control of terminal decimal digits is needed instead. No conclusion for these places is implied by the present 3-adic theorem.

If all fixed-prime coefficient limits were supplied, the resulting signed arithmetic forms would converge pointwise to Q_W on D because each test sees finitely many prime powers. That statement would still say nothing about positivity of the approximants.

For noncompact tests, growing supports, global Dirichlet series, or operator limits on a common Hilbert space, additional uniform estimates are needed.

| Notion of limit | What it actually provides |
|---|---|
| Pointwise convergence of local scalar coefficients | Convergence of finite linear combinations of those coefficients only. |
| Convergence of all Gram matrix elements q_n(f,g) on D | If every q_n is positive, the limiting form is positive on D. This is sufficient for the Weil criterion. |
| Strong convergence of T_n f in a common target Hilbert space | Gives convergence of Gram matrix elements for each f,g. |
| Weak convergence of T_n f | Does not give convergence of their norms or Gram forms; orthonormal vectors are a counterexample. |
| Weak operator convergence of bounded positive A_n on one Hilbert space | Preserves positivity of the limiting bounded operator. |
| Strong resolvent or closed-form convergence for unbounded operators | Requires common domain/core and the relevant semiboundedness and convergence hypotheses; it is not implied by coefficient convergence. |

### 5.8 A valid non-circular operator replacement on bounded log intervals

Fix L>0 and X_L=L^2(-L,L), extending functions by zero. Let V_L be the completion of C_c^infinity(-L,L) in the norm

\[
\|h\|_{\log}^2=
\frac1{2\pi}\int_{\mathbb R}
\bigl(1+\log(2+|t|)\bigr)|\widehat h(t)|^2dt.
\tag{FA1}
\]

The digamma series gives, for a>0,

\[
\Re\psi(a+ib)-\psi(a)
=\sum_{n\ge0}\frac{b^2}{(n+a)((n+a)^2+b^2)}\ge0.
\]

Thus Omega(t)>=Omega(0), where Omega(0)=-gamma-pi/2-3 log 2-log pi. Its asymptotic expansion gives Omega(t)=log|t|-log(2pi)+o(1). Hence the archimedean form is closed and bounded below on V_L.

The pole form is a bounded rank-two form on X_L, because e^(u/2) and e^(-u/2) belong to L^2(-L,L). Only finitely many compressed translations occur in the prime contribution. Thus Q_W restricted to V_L is a closed semibounded form and defines a self-adjoint operator H_L by the form representation theorem, without assuming RH.

This is a rigorous signed operator realization. The missing assertion is H_L>=0 for every L. If it holds, H_L^(1/2) is a valid local factor. Taking its positive part in advance changes the form and is not a solution.

### 5.9 Why a global L^2 adjoint cannot be taken for granted

Equation (32) concerns a map from a test-function space; no Hilbert norm on its source was specified. Therefore T^*T in (33) is initially only notation for a form.

There is a real obstruction to interpreting it automatically as a closed operator on unweighted L^2(R,du). Even assuming RH, the spectral map h -> (hat h(gamma))_gamma is not closable on this source space.

To see this, choose a zero ordinate gamma_0, choose phi in C_c^infinity with integral 1, and set

\[
h_L(u)=L^{-1}\phi(u/L)e^{-i\gamma_0u}.
\]

Then ||h_L||_2 ->0, while hat h_L(t)=hat phi(L(t-gamma_0)). The values at gamma_0 are 1 and the values at all other distinct zero ordinates tend to zero in ell^2. This last assertion follows from rapid decay, the positive separation from the fixed ordinate gamma_0, and the O(T log T) zero-count bound. Thus the spectral images converge to a nonzero vector.

In particular the Weil form, under RH, is not closable with this global unweighted L^2 norm. Fixed-support form domains as above avoid this problem. A sufficiently weighted Sobolev source is another option. Positivity of a form on D and closability with respect to an arbitrarily chosen Hilbert norm are distinct requirements.

### 5.10 The exact RH equivalence

For the conventions (W1),

\[
\boxed{\mathrm{RH}\iff Q_W(f,f)\ge0
\quad\hbox{for every }f\in C_c^\infty(\mathbb R_+^\times).}
\tag{RH}
\]

If RH holds, (W7) becomes the absolutely convergent sum sum_gamma |Mf(1/2+i gamma)|^2.

For completeness, the converse can be proved directly on compact smooth tests. In logarithmic coordinates put z=rho-1/2 and tau(z)=-bar z. Suppose z_0!=tau(z_0). Laplace transforms of compact smooth functions can interpolate arbitrary values at any finite set of distinct complex points: a failure would give a linear relation among distinct exponentials, which is impossible.

Choose a transform G with G(z_0)=G(tau z_0)=1. Its rapid decay leaves only finitely many other zero locations where either |G(z)| or |G(tau z)| is >=1/2. Choose another transform K with values 1 and -1 at the target pair and zero at those finitely many other locations. For the convolution power with transform G^N K, the target pair contributes -2 times its multiplicity. Every other contribution has total absolute value O(4^(-N)), since sum |K(z)K(tau z)| converges. The form is negative for large N.

One may additionally impose K(1/2)=K(-1/2)=0, so the pole-annihilating test class also suffices. But a single bounded support class does not contain the enlarging convolution powers in this proof. Positivity only on a finite-dimensional family, or only at one support scale, is not this criterion.

### 5.11 Mandatory circularity tests

| Test | Outcome |
|---|---|
| Haar tautology | Passed as an audit: the Haar Tate limit reproduces an already known Euler factor; no positivity conclusion is drawn from it. |
| Independent positivity | Local Gram operators are independently positive. Positivity of the global signed form has not been proved. |
| Vanishing limit | Unrenormalized excesses vanish; every polynomial rescaling also vanishes at fixed depth. No nonvanishing Weil operator has emerged. |
| Global sign | Individual signed prime operators are indefinite; the exact two-bump obstruction is (O1). |
| Archimedean completion | Gamma and pole terms have been derived with fixed signs. Their incorporation into a positive coupled construction is missing. |
| Prime uniformity | Only p=3 has been proved. Fixed-test compact support makes the arithmetic sum finite but does not manufacture the missing local theorems. |
| Topology | Scalar convergence and Gram-form convergence are distinguished; a specific global L^2 closability failure is exhibited. |
| Clifford novelty | The finite Clifford realization adds no positivity statement beyond the finite Gram identities. |
| Spectral constraint | The current local limit gives Euler factors and no new restriction on zeta zeros. The full Weil identity would be a different theorem. |
| Finite counterexamples | Period extensions, ordinary depth-two reality, positive finite logarithmic weights, independent signed-prime norms, and positive naive truncations all fail explicit tests. |

## Deliverable 6. A minimal precise missing lemma

The missing step can be expressed as a concrete bounded-operator inequality, without defining any operator through conjectural positivity.

Fix L>0 and retain X_L,V_L from (FA1). Set

\[
c=1-\Omega(0),\qquad
a_L(h,g)=\frac1{2\pi}\int
(\Omega(t)+c)\widehat h(t)\overline{\widehat g(t)}dt.
\]

Let A_L>=I be the self-adjoint operator of this positive closed form. Let P_L denote the bounded rank-two pole operator on X_L. If J_L is zero extension, define

\[
B_{\rm fin,L}=
\sum_{p^a\le e^{2L}}
\frac{\log p}{p^{a/2}}\,
J_L^*(U_{a\log p}+U_{-a\log p})J_L,
\]

\[
R_L=cI+B_{\rm fin,L}-P_L,\qquad
C_L=A_L^{-1/2}R_LA_L^{-1/2}.
\tag{M1}
\]

All these objects are constructed from explicit finite arithmetic, the real-place symbol, and bounded functional calculus of the already positive A_L. There is no RH assumption in their definitions. C_L is bounded and self-adjoint. In fact it is compact: bounded support and the logarithmic Fourier weight give a compact embedding V_L into X_L, by controlling frequency tails by 1/log T and using compactness on a bounded spatial interval.

The exact identity is

\[
Q_W(h,g)=
\left\langle
(I-C_L)A_L^{1/2}h,\ A_L^{1/2}g
\right\rangle,\qquad h,g\in V_L.
\tag{M2}
\]

The minimal missing comparison lemma at support scale L is

\[
\boxed{\lambda_{\max}(C_L)\le1.}
\tag{M3}
\]

Equivalently R_L<=A_L in quadratic-form order. If proved, it gives the actual factor

\[
T_L=(I-C_L)^{1/2}A_L^{1/2}
\]

with the required Gram identity at that support scale.

The hypotheses are explicit: the centered Weil normalization, the fixed interval, the stated closed-form domain, the exact gamma symbol, and the exact prime-power translations. No finite-K approximation is substituted for the desired form.

Existing local lemmas do not imply (M3): they control nonnegative Fourier norms of residue deviations, whereas (M3) compares the real place, two pole directions, and all translations visible at scale L. The prime terms in this comparison are themselves indefinite.

Proving (M3) for one chosen L would be a finite-support advance and would require further work for RH. Proving it for every L, or for an unbounded sequence of L, would imply RH directly. It is not presented as an already proved lemma or as a reduction that makes the central difficulty disappear.

For a specifically Mighty-K route, the additional obligation is to derive this comparison from genuinely coupled arithmetic operators. Merely replacing the finite-prime weights by their Haar limits or taking square roots after assuming (M3) does not do that.

## Deliverable 7. Research verdict

**What is genuinely proved?**

The period-three theorem, its depth-two period-nine variant, the exact reversal phase and corrections, every supplied finite regression value, exact small-K local coefficients, finite Clifford matrix-element identities, sharp shell-error bounds, coefficientwise local Tate convergence, and quantitative total-variation equidistribution whenever 3^r=o(sqrt K). The argument also proves two concrete no-go results for the proposed global assembly and gives a valid signed self-adjoint realization on every bounded log interval.

**What remains open?**

A non-circular coupled operator whose positive Gram form equals the actual Weil form; the comparison (M3) at arbitrarily large support scales; additional fixed-prime theories if all weights are to come from permutations; analytic local convergence beyond the justified domain; and a meaningful, non-tautological renormalized collision limit related to global spectral data. Nothing here proves RH.

**What is the highest-value next calculation or theorem?**

Work on C_L, including its pole directions and exact real-place term. Start with a support interval containing several prime translations, compute certified Galerkin bounds with an explicit tail estimate, and identify a cross-place inequality that controls its largest eigenvalue as L grows. The useful target is an upper bound by 1, not additional numerical agreement with Haar shell coefficients. A local improvement alone cannot overcome (O1) or (O4).

## References for established global facts

1. Jean-Francois Burnol, *The Explicit Formula in Simple Terms*, 1998, especially the sections on Weil's criterion and the classical explicit formula: https://arxiv.org/abs/math/9810169 and https://arxiv.org/pdf/math/9810169 .
2. Enrico Bombieri, *The Riemann Hypothesis*, official Clay Mathematics Institute problem description, Section V: https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf .
3. NIST Digital Library of Mathematical Functions, equation 5.9.16 for the digamma integral: https://dlmf.nist.gov/5.9.E16 .

The local combinatorial proofs, constants, finite arithmetic, and obstruction arguments in this audit are supplied explicitly for independent verification. No claim of priority over the mathematical literature is made.
