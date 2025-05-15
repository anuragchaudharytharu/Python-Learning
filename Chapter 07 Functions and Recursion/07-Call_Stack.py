'''
    CALL STACK

        Its a container that store tasks like variable, function, loops etc in memory layer by layer

        Priority to complete for multiple tasks and their layers is of first come first service format based on the provided conditions

        Call Stack checks every layer of memory of certain task. When the end layer of the task is completed, it first delete that end layer and then looks for other immediate layer below it. Again it checks if that layer is completed. If yes, then it delete that layer and move to the immediate layer below it. Again it repeat the cycle of checking and deleting until it has deleted all of the layer od memory task inside the call stack
'''