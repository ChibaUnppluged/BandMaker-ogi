import java.util.ArrayList;
import java.io.*;
public class AnswerGathering{
    // 1-1の回答
    // 増加列のうち最も長いものを検索し出力する
    public void answer_1(String inputLine){
        InputConversion inputConversion = new InputConversion();
        InternalProcessing internalProcessing = new InternalProcessing();
        ArrayList<Integer> inputList = inputConversion.ToIntegerArray(inputLine);
        String output = internalProcessing.increasingSearch(inputList);
        System.out.println(output);
    }
    // 1-2の回答
    // 同値部分列のうち最も長いものを検索し出力する
    public void answer_2(String inputLine){
        InputConversion inputConversion = new InputConversion();
        InternalProcessing internalProcessing = new InternalProcessing();
        ArrayList<Integer> inputList = inputConversion.ToIntegerArray(inputLine);
        String output = internalProcessing.equivalentSearch(inputList);
        System.out.println(output);
    }
    // 1-3の回答
    public void answer_3(String inputLine){
        InputConversion inputConversion = new InputConversion();
        InternalProcessing internalProcessing = new InternalProcessing();
        ArrayList<String> inputList = inputConversion.ToStringArray(inputLine);
        String output = internalProcessing.sameCharSearch(inputList);
        System.out.println(output);
    }
}