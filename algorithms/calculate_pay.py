def calculate_pay(daily_work_hours):
  pay_list = []
  consecutive_days = 0
  consecutive_days_basic_pay = 0
  consecutive_idx = 1
  
  for k, h in enumerate(daily_work_hours):
    # Calculate each day's Basic Pay
    total_daily_pay = 0
    if h <= 8:
      total_daily_pay += h*10
    else:
      total_daily_pay += 8*10

    h -= 8
    
    # Calculate additional pay
    if h>0:
      if 0 < h <= 2:
        total_daily_pay += h * (10 * 50/100) + 10
      else:
        total_daily_pay += 2 * (10 * 50/100) + 10
        total_daily_pay += (h-2) * 10 + 10
        
    # Count consecutive days  
    if consecutive_idx>0 and consecutive_idx < len(daily_work_hours)-1:
      if sum([ daily_work_hours[consecutive_idx-1], daily_work_hours[consecutive_idx], daily_work_hours[consecutive_idx+1] ]) >= 30:
        consecutive_days += 1
        consecutive_idx += 3
      else:
        consecutive_idx += 1
        
    pay_list.append(total_daily_pay)

  # Calculate consecutive payment
  if consecutive_days > 0:
    consecutive_days_basic_pay = consecutive_days * 3 * 10 + consecutive_days * 50
  
  return sum(pay_list) + consecutive_days_basic_pay

print calculate_pay([8,9,4,9,12,10,10])  
  
# if __name__ == '__main__':
#   daily_work_hours = [8,9,4,9,12,10,7]
#   print calculate_pay(daily_work_hours)
