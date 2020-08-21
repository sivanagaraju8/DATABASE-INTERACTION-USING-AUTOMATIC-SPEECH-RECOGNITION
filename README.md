# DATABASE Interaction Using Automatic Speech Recognition
Automatic Speech Recognition or ASR is a technology that allows human beings to use their voices to speak with a computer interface\.
Database Interaction Voice Assistant to Access the MySQL Databases through voice commands. <br />
Voice Command checks with initialized set of commands then maps with SQL Queries. <br />
Executes Mapped Sql queries, outputs the Data of the respective selected database or Table.

# Getting started

## Prerequisites
* [Python](http://python.org)
* [SQL](https://www.mysql.com/) 
* [MySQL Connector](#)
* [Speech Recognition](#)
* [PlaySound](#)
* [gTTS](#)
* [random](#)
* [Pandas](#)

## Installing
* install [Python](http://python.org)
* install [SQL](https://www.mysql.com/) 
* install [MySQL Connector](#)
* install [Speech Recognition](#)
* install [PlaySound](#)
* install [gTTS](#)
* install [random](#)
* install [Pandas](#)
## Built with 
* [Python](http://python.org)
* [SQL](https://www.mysql.com/)

### Project Description

* Voice Input

       input with human Voice signal 
* Microphone 

      (a) : Voice/Analog Signal collection through the microphone.
      
      (b) : Digital conversion by sampling.
      
      (c) : Noise cancellation.
      
      (d) : Here Frame Rate: 44.1 kHz
                 Chunk Value: 1024

* Automatic Speech Recognition

      (1) : Automatic Speech Recognition is a technology that allows humans to use their voices to speak with a computer interface.
      
      (2) : Speech recognition with Google API.
      
      (3) : Transcription generation.
      
      (4) : Text filtration.
      
* Text to SQL Command Conversion

      (a) : Initializing set of user commands.
            " --- Connect to Database "
            " --- Show Databases "
            " --- Select Database [Name] "
            " --- Show TABLES "
            " --- Show TABLE Data "
            " --- Say abort or end or terminate to exit "
            
      (b) : Mapping of transcripted text to given commands.
      
      (c) : If mapped , commands to SQL query conversion.
      
      (d) :Else, retry and iterate the process.

* Database Interface

      (1): Database interface process takes place.

      (2): Setup to establish secure connection with main database storage.

      (3): Execute the predicted or matched SQL query.

      (4): Retrieve data from database.


* Output Interaction with Voice Assistance Using gTTS

      Prints retrieved data output on the screen.

      Interact and describe the output with voice assistance using gTTS(Google Text To Speech).

      This feature acts as Google Assistant for this project.
      
### Block Diagram 
 ![Block Diagram](https://github.com/sivanagaraju8/DATABASE-INTERACTION-USING-AUTOMATIC-SPEECH-RECOGNITION/blob/master/Block_Diagram.png)

### Video Demonstration
  * (https://www.youtube.com/watch?v=DJw2tdFiTmQ)
# Authors
* #### Gamidi Siva Nagaraju - [(https://www.linkedin.com/in/siva-nagaraju/)](https://www.linkedin.com/in/siva-nagaraju/)
