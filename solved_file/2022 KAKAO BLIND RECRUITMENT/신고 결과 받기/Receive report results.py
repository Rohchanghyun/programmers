from collections import defaultdict
def solution(id_list, report, k):
    report_count = defaultdict(list)
    answer_count = {}
    answer = []
    
    report = set(report)
    for s in id_list:
        answer_count[s] = 0
        
    for r in report:
        report_from,report_to = r.split(' ')
        report_count[report_to].append(report_from)
            
    for key,val in report_count.items():
        if len(val) >= k:
            for i in val:
                answer_count[i] += 1
                
    for key,val in answer_count.items():
        answer.append(val)
        
    return answer