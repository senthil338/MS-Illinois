package edu.illinois.storm;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;
import org.apache.storm.spout.SpoutOutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.IRichSpout;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;

/** a spout that generate sentences from a file */
public class FileReaderSpout implements IRichSpout {
  private SpoutOutputCollector _collector;
  private TopologyContext _context;
  private String inputFile;
  private FileReader fileReader;
  private boolean isDone = false;

  // Hint: Add necessary instance variables if needed

  @Override
  public void open(Map conf, TopologyContext context, SpoutOutputCollector collector) {
    this._context = context;
    this._collector = collector;
    String filename = conf.get("input").toString();
    try {
 	fileReader = new FileReader(filename);
    } 
    catch (IOException e){
                  	 e.printStackTrace();
    }
    /* ----------------------TODO-----------------------
    Task: initialize the file reader
    ------------------------------------------------- */

    // END

  }

  // Set input file path
  public FileReaderSpout withInputFileProperties(String inputFile) {
    this.inputFile = inputFile;
    return this;
  }

  @Override
  public void nextTuple() {
    if(isDone){
       try {
            Thread.sleep(1000);
       }
       catch (InterruptedException e){
              // interruption is normal
       }
    }
    BufferedReader reader = new BufferedReader(fileReader);
    String line;
    try {
         while ((line = reader.readLine()) != null){
	       line = line.trim();
	       if(line.length() > 0){
                  _collector.emit(new Values(line));
               }
         }
    }
    catch (IOException e){
          e.printStackTrace();
    }
    finally{  
          isDone = true;
    }
    /* ----------------------TODO-----------------------
    Task:
    1. read the next line and emit a tuple for it
    2. don't forget to add a small sleep when the file is entirely read to prevent a busy-loop
    ------------------------------------------------- */
    // END
  }

  @Override
  public void declareOutputFields(OutputFieldsDeclarer declarer) {
    /* ----------------------TODO-----------------------
    Task: define the declarer
    ------------------------------------------------- */
    declarer.declare(new Fields("word"));
    // END
  }

  @Override
  public void close() {
    /* ----------------------TODO-----------------------
    Task: close the file
    ------------------------------------------------- */
    try {
	 fileReader.close();
    } 
    catch (IOException e) {
         e.printStackTrace();
    }
    // END

  }

  public void fail(Object msgId) {}

  public void ack(Object msgId) {}

  @Override
  public void activate() {}

  @Override
  public void deactivate() {}

  @Override
  public Map<String, Object> getComponentConfiguration() {
    return null;
  }
}
