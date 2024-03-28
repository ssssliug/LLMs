from zhipuai import ZhipuAI
import json

client = ZhipuAI(api_key="6e2bbde6def454ee8eaf6bf86450312b.a2DOXtB2jmWgZGeA") # 填写您自己的APIKey
correct_answers = 0
                    
data_test=[]

with open('QAtest/output.json', 'r', encoding='utf-8') as file:
    test_cases = json.load(file)
    total_questions = len(test_cases)
    for case in test_cases:
        question = case['question']
        options = case['options']
        correct_label = case['answer']
        response = client.chat.completions.create(
            model="glm-3-turbo",  # 填写需要调用的模型名称
            messages=[
             {"role": "user", "content":  f"根据内容从选项中选出最合适的一项，只输出对应选项的字母，不输出其他任何内容。{question}{options}"},],)

        print(response.choices[0].message.content)

        generated_answer = response.choices[0].message.content  # 这应该是模型的输出


        if generated_answer == correct_label:
            correct_answers += 1
        else:
                data_test.append(
                    {
                    'question': question,
                    'options': options,
                    'correct_answers': correct_label,
                    'error_answers': generated_answer})
            
accuracy = correct_answers / total_questions if total_questions > 0 else 0
data_test.append(
                    {
                        'correct_answers': correct_answers,
                        'total_questions': total_questions,
                        'accuracy': accuracy})

print(f'正确答案数量: {correct_answers}/{total_questions}')
print(f'正确率: {accuracy:.2%}')


json_data = json.dumps(data_test, ensure_ascii=False,indent=4)
with open('QAtest/test_results.json', 'w', encoding='utf-8') as file:
                    file.write(json_data)   



