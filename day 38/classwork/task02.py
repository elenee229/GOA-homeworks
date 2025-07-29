#2) შექმენით manual_max ფუნქცია რომელსაც პარამეტრად გადაეცემა სია და აბრუნებს ყველაზე დიდ მნიშვნელობას. ასევე შექმენით manual_len ფუნქცია რომელიც თვლის გადაცემული მიმდევრობის სიგრძეს
def manual_max(arr):
    if not arr:
        return None
    max_val=arr[0]
    for item in arr:
        if item>max_val:
            max_val=item
        return max_val
    
    def manual_len(arr):
        num1=0
        for i in arr:
            num1 += 1
        return num1