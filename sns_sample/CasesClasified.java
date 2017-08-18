public class CasesClasified{
    public void from_1_to_3(String[] argument){
        int arg1 = Integer.parseInt(argument[0]);
        if(argument.length==1){
            System.out.println("");
            return;
        }
        String arg2 =argument[1]; 
        AnswerGathering answerGathering = new AnswerGathering();
        switch(arg1){
            case 1:
            answerGathering.answer_1(arg2);
            break;
            case 2:
            answerGathering.answer_2(arg2);
            break;
            case 3:
            answerGathering.answer_3(arg2);
            break;

        }

    }

}