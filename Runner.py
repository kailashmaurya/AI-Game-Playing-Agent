import os
import time

for i in xrange(109):
    # Copy test case from \cases directory to current directory, this overwrites the previous input.txt file
    os.system('copy /Y .\cases\{0}.in .\input.txt'.format(i))

    print("-->On test case #{0}<--".format(i))
    start_time = time.time()
    
    # Run the script on currently copied input file
    os.system('python GamePlayingAgent.py')
    
    # Display the actual execution time for the input
    print("Runing time: {0}ms".format(int((time.time() - start_time) * 1000)))
    
    # Compare the output generated by GamePlayingAgent.py and the correct output present in cases directory
    os.system('FC .\output.txt .\cases\{0}.out'.format(i))
    
    # Copy output.txt file to cases directory
    os.system('copy /Y .\output.txt .\cases\Your_output{0}.txt'.format(i))
