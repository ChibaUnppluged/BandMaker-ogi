import java.lang.Boolean;
import java.util.ArrayList;
public class InternalProcessing{
    // 位置変数
        int start=0;
        int end = 0;
        // 増加列の大きさを一時的に保持する変数
        int ContinuityNum = 0;
        // メソッドが返す値を保持する変数
        String returnStr="";

    // sameCharSearch
    // ArrayList<String>を受け取り最大の同字部分列をString型で返す.
    public String sameCharSearch(ArrayList<String> inputList){
       for ( int i=0;i<inputList.size()-1; i++){
            // i+1番目がi番目と等しければendを更新
            // そうでなければContinuityNumをチェック
            if (inputList.get(i).equals(inputList.get(i+1))){
                end = i+1;
            }
            else{
                // end-startがContinuityNumの大きさより大きければ
                // returnStrとContinuityNumを更新
                if (ContinuityNum<end-start){
                    returnStr = stringFromArrayStr(inputList, start, end);
                    ContinuityNum = end-start;
                }
                // startを現在の位置まで更新
                start = i+1;
            }
        } 
        if (ContinuityNum==0&&(end-start)!=0){
            returnStr=stringFromArrayStr(inputList, start, end);
        }
        return returnStr;
    }
    // equivalentSearch
    // ArrayList<Integer>を受け取り最大の増加列をString型で返す.
    public String equivalentSearch(ArrayList<Integer> inputList){
        // はじめから大きさ-1番目までをチェック
        for ( int i=0;i<inputList.size()-1; i++){
            // i+1番目がi番目と等しければendを更新
            // そうでなければContinuityNumをチェック
            if (inputList.get(i)==inputList.get(i+1)){
                end = i+1;
            }else{
                // end-startがContinuityNumの大きさより大きければ
                // returnStrとContinuityNumを更新
                if (ContinuityNum<end-start){
                    returnStr = stringFromArrayInt(inputList, start, end);
                    ContinuityNum = end-start;
                }
                // startを現在の位置まで更新
                start = i+1;
            }

        }
        if (ContinuityNum==0&&(end-start)!=0){
           returnStr = stringFromArrayInt(inputList, start, end);
        }
        return returnStr;
    } 
    //increasingSearch
    // ArrayList<Integer>を受け取り最大の増加列をString型で返す.
    public String increasingSearch(ArrayList<Integer> inputList){
        
        // はじめから大きさ-1番目までをチェック
        for ( int i=0;i<inputList.size()-1; i++){
            // i+1番目がi番目+1になっていればendを更新
            // そうでなければContinuityNumをチェック
            if (arithmeticCheck(inputList.get(i), inputList.get(i+1), 1)){
                end = i+1;
            }else{
                // end-startがContinuityNumの大きさより大きければ
                // returnStrとContinuityNumを更新
                if (ContinuityNum<end-start){
                    returnStr = stringFromArrayInt(inputList, start, end);
                    ContinuityNum = end-start;
                }
                // startを現在の位置まで更新
                start = i+1;
            }

        }
        //入力すべてが増加列の際の処理
        if (ContinuityNum==0&&(end-start)!=0){
           returnStr = stringFromArrayInt(inputList, start, end);
        }
        return returnStr;
    

    }
    // StringFromArrayList
    // ArrayListのstartからendまでの値を取り出し連続した文字列として返す.
    public String stringFromArrayInt(ArrayList<Integer> list,int start,int end){
        // 返す値
        String returnStr="";
        // start番目からend番目まで取り出してreturnStrに結合
        for (int i = start;i<=end;i++){
            returnStr = returnStr + String.valueOf(list.get(i));
        }
        // return
        return returnStr;
    }
    public String stringFromArrayStr(ArrayList<String> list,int start,int end){
        // 返す値
        String returnStr="";
        // start番目からend番目まで取り出してreturnStrに結合
        for (int i = start;i<=end;i++){
            returnStr = returnStr + list.get(i);
        }
        // return
        return returnStr;
    }
    // numSmallよりnumBigのほうがdifferenceの値だけ大きければtrueを返し,そうでなければfalseを返す
    public Boolean arithmeticCheck(int numSmall,int numBig,int difference){
        // 返す値
        Boolean checkAnswer;
        // 値のチェック
        if (numBig-numSmall==difference){
            checkAnswer=true;
        }else{
            checkAnswer = false;
        }
        // return
        return checkAnswer;
        }
}