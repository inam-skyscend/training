import cProfile
import pstats

pr = cProfile.Profile()
pr.enable()

f1 = open('/home/inamhusain/Workspace/training/Exercise/python exercise 1/Que-15.py','r')
f_str = f1.read()
pr.run(f_str)

pr.disable()
ps=pstats.Stats(pr)
ps.print_stats()

