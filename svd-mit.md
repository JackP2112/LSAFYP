### Singular Value Decomposition
####  - Gilbert Strang MIT OpenCourseWare
[Youtube](https://www.youtube.com/watch?v=rYz83XPxiZo)

Singular Value Decomposition is analogous to eigendecomposition for non-square
matrices.

Instead of finding eigenvalues and eigenvectors, the left and right singular
vectors are found as well as the matrix of singular values.
The left and right singular values correspond to eigenvectors of AtA and AAt,
and the singular values to the eigenvalues.
Though the dimension is different, the nonzero eigenvalues in each case are the
same, which are the squares of the singular values.

The matrices in the decomposition are an orthogonal matrix Vt, multiplied by the
diagonal matrix Σ, multiplied by another orthogonal matrix U.
The decomposition can therefore be visualised as a rotation, scaling and a final
rotation.

By convention, the singular values are ordered from highest to lowest, allowing
for a low-rank approximation to be taken by ignoring the lower values and taking
only the principal components.
