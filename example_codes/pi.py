import numpy as np
from mpi4py import MPI


def main():
  # int n, myid, numprocs, i;
  PI25DT = 3.141592653589793238462643
  # double mypi, pi, h, sum, x

  numprocs = MPI.COMM_WORLD.Get_size()
  myid = MPI.COMM_WORLD.Get_rank()

  print("worker %d of %d" % (myid,numprocs))

  # /* Number of intervals */
  n = 25

  MPI.MPI_WORLD.bcast(n, root=0)
  h = 1.0 /  float(n)
  sum = 0.0
  for i in xrange(myid+1,n+1,numprocs):
       x = h * (float(i) - 0.5)
       sum += ( 4.0 / (1.0 + x*x) )
  mypi = h * sum;
  MPI.MPI_WORLD.Reduce([mypi,MPI.DOUBLE], [pi,MPI.DOUBLE], op=MPI.SUM, root=0)

  if myid == 0:
      print("pi is approximately %.16f, Error is %.16f\n" % (pi, fabs(pi - PI25DT)))

if __name__ == '__main__':
   main()
