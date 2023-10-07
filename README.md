Python implementation of orbital mechanics algorithms from Orbital Mechanics for Engineering Students by Howard Curtis. `numpy` is the only external dependency but `pytest` is required for running tests. All algorithms implemented have at least one unit test to validate the implementation. Helper functions used directly by an algorithm may not have unit tests.

## Algorithms

### Algorithm 3.1: Solution of Kepler’s Equation by Newton’s Method
This function uses Newton’s method to solve Kepler’s equation E - e*sin(E) = M for the eccentric anomaly, given the eccentricity and the mean anomaly.

### Algorithm 3.2: Solution of Kepler’s Equation for the Hyperbola using Newton’s Method

This function uses Newton’s method to solve Kepler’s equation for the hyperbola e*sinh(F) - F = M for the hyperbolic eccentric anomaly, given the eccentricity and the hyperbolic mean anomaly.

### Algorithm 3.3: Solution of the Universal Kepler’s Equation using Newton’s Method

This function uses Newton’s method to solve the universal Kepler equation for the universal anomaly.

### Algorithm 3.4: Calculation of the Statevector (r, v) given the Initial State Vector (r0, v0) and the Time Lapse Δt

This function computes the state vector (R,V) from the initial state vector (R0,V0) and the elapsed time.

### Algorithm 4.1: Calculation of the Orbital Elements from the State Vector

This function computes the classical orbital elements (coe) from the state vector (R,V) using Algorithm 4.1.

### Algorithm 4.2: Calculation of the State Vector from the Orbital Elements

This function computes the state vector (r,v) from the classical orbital elements (coe).

### Algorithm 5.1: Gibbs’ Method of Preliminary Orbit Determination

This function uses the Gibbs method of orbit determination to compute the velocity corresponding to the second of three supplied position vectors.