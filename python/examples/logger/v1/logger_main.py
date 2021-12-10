# author : Amit Singh Sansoya [@amit3200]
"""
interface Logger { 
	/**
	* When a process starts, it calls 'start' with processId and startTime.
	*/
	void start(String processId, long startTime);
	
	/**
	* When the same process ends, it calls 'end' with processId and endTime.
	*/
	void end(String processId, long endTime);

	/**
	* Prints the logs of this system sorted by the start time of processes in the below format
	* {processId} started at {startTime} and ended at {endTime}
	*/
	void log();
}
"""

from my_logger1 import MyLogger

log = MyLogger()
log.start(process_id = "1", start_time = 100)
log.start(process_id = "2", start_time = 101)
log.finish(process_id = "2", end_time = 102)
log.start(process_id = "3", start_time = 102)
log.start(process_id = "4", start_time = 103)
log.finish(process_id = "1", end_time = 104)
log.log()

log.finish(process_id = "3", end_time = 109)
print("[Transition] 1 : ", "=" * 100)
log.log()

log.start(process_id = "4", start_time = 108)
log.finish(process_id = "3", end_time = 118)
print("[Transition] 2 : ", "=" * 100)
log.log()

