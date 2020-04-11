package edu.illinois.storm;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;
import java.util.Iterator;
import java.util.Set;
import java.util.HashSet;
/** a bolt that finds the top n words. */
public class TopNFinderBolt extends BaseRichBolt {
  private OutputCollector collector;
  private int N;
  private Map<String, Integer> map;
  private PriorityQueue<String> pq;
  private Set<String> seen;
  private long intervalToReport = 20;
  private long lastReportTime = System.currentTimeMillis();
  // Hint: Add necessary instance variables and inner classes if needed


  @Override
  public void prepare(Map conf, TopologyContext context, OutputCollector collector) {
    this.collector = collector;
    this.map = new HashMap<>();
    this.pq = new PriorityQueue<>((s1, s2) -> map.get(s1) - map.get(s2));
    this.seen = new HashSet<>();
  }

  public TopNFinderBolt(int N) {
    /* ----------------------TODO-----------------------
    Task: set N
    ------------------------------------------------- */

		// End
		this.N = N;
  }

  @Override
  public void execute(Tuple tuple) {
    /* ----------------------TODO-----------------------
    Task: keep track of the top N words
		Hint: implement efficient algorithm so that it won't be shutdown before task finished
		      the algorithm we used when we developed the auto-grader is maintaining a N size min-heap
    ------------------------------------------------- */
                String word = tuple.getString(0);
		Integer i = tuple.getInteger(1);

		Integer cnt = map.get(word);
		if(cnt == null){
			map.put(word, i);
		}else map.put(word, i+cnt);
                
		if(seen.add(word)) pq.add(word);
		//if(!pq.contains(word)) pq.add(word);
		if(pq.size()>10){
		   String top = pq.poll();
		   seen.remove(top);
		}
		//String tmp = pq.poll();
		//pq.offer(tmp);
                Iterator itr = pq.iterator();
		StringBuilder sb = new StringBuilder();
		while(itr.hasNext()){
			String str = itr.next().toString();
			if(itr.hasNext()){
				sb.append(str);
				sb.append(", ");
			}else sb.append(str);
		}
                //if (System.currentTimeMillis() - lastReportTime >= intervalToReport) {
			   
			    
			    String topwords = sb.toString();
		            collector.emit(new Values(topwords));
		 //          lastReportTime = System.currentTimeMillis();
	        //}
		// End
  }

  @Override
  public void declareOutputFields(OutputFieldsDeclarer declarer) {
    /* ----------------------TODO-----------------------
    Task: define output fields
		Hint: there's no requirement on sequence;
					For example, for top 3 words set ("hello", "word", "cs498"),
					"hello, world, cs498" and "world, cs498, hello" are all correct
    ------------------------------------------------- */
    declarer.declare(new Fields("top-N"));
    // END
  }

}
