import java.io.*;
import java.lang.reflect.Array;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.*;

public class MP0 {

    private class CountWord implements Comparable<CountWord> {
		public CountWord(Integer count, String word) {
	    this.count = count;
	    this.word = new String(word);
	}

	public Integer getCount() { return count; }
	public String getWord() { return word; }

	public int compareTo(CountWord other) {
        if (this.getCount().equals(other.getCount())) 
        {
		    return this.getWord().compareTo(other.getWord());
	    }
        else 
        {
        
            return other.getCount().compareTo(this.getCount());
	    }
	}

	Integer count;
	String word;
    };

    Random generator;
    String userName;
    String delimiters = " \t,;.?!-:@[](){}_*/";
    //String inputFileName = "C:\\Senthil\\Masters\\CS 498 CCA\\MP0-master\\MP0-master\\input.txt";
    String[] stopWordsArray = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"};

    public MP0(String userName) {
        this.userName = userName;
    }


    public Integer[] getIndexes() throws NoSuchAlgorithmException {
        Integer n = 10000;
        Integer number_of_lines = 50000;
        Integer[] ret = new Integer[n];
        long longSeed = Long.parseLong(this.userName);
        this.generator = new Random(longSeed);
        for (int i = 0; i < n; i++) {
            ret[i] = generator.nextInt(number_of_lines);
        }
        return ret;
    }

    public String[] process() throws Exception{
        String[] topItems  = new String[20];

        //TODO
        List<String> stopWordsList = Arrays.asList(stopWordsArray);
        BufferedReader reader = null;
          
        int lines = 0;
        int words = 0;
        int unique = 0;
        int skipped = 0;

            reader = new BufferedReader(new InputStreamReader(System.in));
            String text = null;
            Map<String, Integer> wordCount = new HashMap<String, Integer>();
            List<String> fileLines = new ArrayList<String>();
            while((text = reader.readLine()) != null) {
                ++lines;
                fileLines.add(text);
            }

            Integer[] indexes = getIndexes();
            for (int i=0; i<indexes.length; ++i) {
                text = fileLines.get(indexes[i]);
                StringTokenizer st = new StringTokenizer(text, delimiters);
                while(st.hasMoreTokens()) {
                    String word = st.nextToken().trim().toLowerCase();
                    ++words;

                    if (!stopWordsList.contains(word)) {
                        Integer count = wordCount.get(word);
                        if (count == null) {
                            count = new Integer(0);
                            ++unique;
                        }
                        ++count;
                        wordCount.put(word, count);
                    }
                    else {
                        ++skipped;
                    }
                }
            }
            
            List<CountWord> countWords = new ArrayList<CountWord>();
            for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {
                String word = entry.getKey();
                Integer count = entry.getValue();
                CountWord cwt = new CountWord(count, word);
                countWords.add(cwt);
            }
            
            Collections.sort(countWords);
            Iterator<CountWord> it = countWords.iterator();
            int resIdx = 0;
            while(it.hasNext()) {
                CountWord cwt = (CountWord) it.next();
                topItems[resIdx] = cwt.getWord();
                if (++resIdx == 20) {
                    break;
                }
            }
        
     
        return topItems;
    }

    public static void main(String args[]) throws Exception {
    	if (args.length < 1){
    		System.out.println("missing the argument");
    	}
        else
        {
    		String userName = args[0];
	    	MP0 mp = new MP0(userName);
	    	String[] topItems = mp.process();

	        for (String item: topItems){
	            System.out.println(item);
	        }
	    }
	}

}
