import java.util.ArrayList;
import java.io.*;
import java.io.IOException;
// 入力を適切な値に直す
public class InputConversion{
    // ToIntegerArray
    // 一行の文字列をArrayListにInt型で一文字ずつ入れたものを返す
    public  ArrayList<Integer> ToIntegerArray(String inputLine){
        ArrayList<Integer> returnList = new ArrayList<Integer>();
        // 文字列を一文字図ずつ配列に格納
        String[] strList=  inputLine.split("");
        // 配列をInt型に直し,ArrayListに格納
        for (int i=0;i<strList.length;i++){
            returnList.add(Integer.parseInt(strList[i]));
        }

        return returnList;
    } 
    // ToStringArray
    // 一行の文字列をArrayListにString型で一文字ずつ入れたものを返す
    public  ArrayList<String> ToStringArray(String inputLine){
        ArrayList<String> returnList = new ArrayList<String>();
        // 文字列を一文字図ずつ配列に格納
        String[] strList=  inputLine.split("");
        // 配列をInt型に直し,ArrayListに格納
        for (int i=0;i<strList.length;i++){
            returnList.add(strList[i]);
        }

        return returnList;
    } 
}