"""****************************************************************************
 Name:        Log
 Purpose:     Creates and maintains a Log file.

 Author:      Justin L. Rich
Location: Geophysical Institute | University of Alaska, Fairbanks
Contributors:

Copyright:   (c) Justin L. Rich 2012
License:     Although this application has been produced and tested
 successfully, no warranty expressed or implied is made regarding the
 reliability and accuracy of the utility, or the data produced by it, on any
 other system or for general or scientific purposes, nor shall the act of
 distribution constitute any such warranty. It is also strongly recommended
 that careful attention be paid to the contents of the metadata / help file
 associated with these data to evaluate application limitations, restrictions
 or intended use. The creators and distributors of the application shall not
 be held liable for improper or incorrect use of the utility described and/
 or contained herein.
****************************************************************************"""
import stop_watch

class Log ():
    """Log is used to create, update and print information to a Log file.
        Attributes:
            Log Name (optional): A String for the name of the Log file.
            Application (optional): The name of the application the Log file
                is reporting on."""

    __logfile = '' # Global variable - Log file name.
    __content = '' # Global variable - The content of the Log file. This is reprinted
    # in it's entirety every time print line is called. 
    __clock = stop_watch.StopWatch #Global variable - Keeps a reference to the stop watch

    # Create the Log file (.txt file) and populate the first line with
    # Date and time information.
    def __init__ (self, output, log_name = 'Log', app_name = 'Application'):
        """init starts the stop watch, creates the Log '.txt' file and populates 
        it with the current date and time."""
        
        global __clock, __logfile, __content
        __clock = stop_watch.StopWatch()
        __logfile = output + '\\' + log_name + '.txt' # Assemble Log file path and name
        __content = app_name + ' Log File: ' + '\n'
        
        # Assemble Date and Time for the Log file.
        content ='Year: ' + str(__clock.get_year()) + ' |'
        content = content + ' Month: ' + str(__clock.get_month_name()) + ' |'
        content = content + ' Day: ' + str(__clock.get_day()) + ' |'
        content = content + ' Started: ' + str(__clock.get_time()) + '\n' + '\n'

        self.print_line(content)

#______________________________________________________________________________
#***Methods********************************************************************
    def print_line (self, text, supress_ts = False):
        """Prints a line to the Log file. supress_ts (time stamp) allows the user 
        to not include a time stamp. used for adding page breaks"""
        global __content # Accessed in order to add new content.
        if supress_ts == False: # No suppression of time stamp.
            __content = __content + str(__clock.get_elapsed_time()) + ' - ' + text + '\n'
            print text
        if supress_ts == True: # Time stamp suppressed. Used in 'print_break'
            __content = __content + text + '\n'
            print text
        
        # Print old and new content to log file.
        self.print_to_logfile()

    def print_to_logfile (self):
        """ Prints '__content' to the log file overwriting what is currently there.
        this is kept as a separate method so that it can be reprinted from outside
        the module."""
        log = open (__logfile, 'w')
        log.write(__content)
        log.close()

    def print_break (self, num_brks = 1):
        """Prints a line break in the Log file."""
        for _ in range (0, num_brks): self.print_line('', True)
        
    def get_content (self):
        """Returns the string value of __content."""
        return __content

#Driver
def main():
    pass
if __name__ == '__main__':
    main()
