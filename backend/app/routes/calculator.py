from fastapi import APIRouter

router = APIRouter()


@router.post("/calculate/")
# def calulate(
#     init_amount: float,
#     monthly_contribution: float,
#     rate: float,
#     years: int,
# ):
#     rate = rate/100
#     monthly_rate = (1 + rate)**(1/12) - 1
#     '''
#         converte duração anual para duração mensal
#         interest_rate anual ===> mensal

#         total = init * (1+interest_rate)^duration

#         monthly_total = sum y=0 to years-1 {
#             monthly_contr
#                 *
#             (1+annual_growth)**y 
#                 * 
#             [(1+month_rate)**(total_months - 12*y) - (1+month_rate)**(total_months - 12(y+1))]/month_rate
#         }

#         annual_contr_total = sum y=1 to years {
#             annual_contribution 
#                 *
#             (1+annual_growth)**(y-1)
#                 *
#             (1+month_rate)**(total_months - 12*y)
#         }
#     '''

#     total = init_amount * (1+(rate/100))**years

#     monthly_total = 0
#     for year in range(years):
#         monthly_total = monthly_contribution * ((1+monthly_rate)**(duration_in_months - 12*year) - 1)/monthly_rate

#     total += monthly_total




#     return {"Total": total}



def calulate(
    init_amount: float,
    monthly_contribution: float,
    annual_contribution: float,
    interest_rate: float,
    is_interest_rate_annual: bool,
    duration: int,
    is_duration_in_years: bool,
    annual_contribution_growth: float,
):
    # interest_rate not in percentage
    
    if not is_duration_in_years:
        duration_in_years = duration//12
        duration_in_months = duration
    else:
        duration_in_years = duration
        duration_in_months = duration*12
    
    if is_interest_rate_annual:
        monthly_rate = (1 + interest_rate)**(1/12) - 1
    else:
        monthly_rate = interest_rate

    '''
        converte duração anual para duração mensal
        interest_rate anual ===> mensal

        total = init * (1+interest_rate)^duration

        monthly_total = sum y=0 to years-1 {
            monthly_contr
                *
            (1+annual_growth)**y 
                * 
            [(1+month_rate)**(total_months - 12*y) - (1+month_rate)**(total_months - 12(y+1))]/month_rate
        }

        annual_contr_total = sum y=1 to years {
            annual_contribution 
                *
            (1+annual_growth)**(y-1)
                *
            (1+month_rate)**(total_months - 12*y)
        }
    '''

    total = init_amount * (1+monthly_rate)**duration_in_months

    monthly_total = 0
    for year in range(duration_in_years):
        current_monthly_contribution = monthly_contribution * (1+annual_contribution_growth)**year 
        twelve_month_rate = (1+monthly_rate)**(duration_in_months - 12*year) 
        rate_until_the_end = (1+monthly_rate)**(duration_in_months - 12*(year+1))
        monthly_total += current_monthly_contribution * ((twelve_month_rate-rate_until_the_end)/monthly_rate)
    total += monthly_total

    total_annual_contribution = 0
    for year in range(1, duration_in_years+1):
        current_annual_contribution = annual_contribution * (1+annual_contribution_growth)**(year-1)
        rate_until_the_end = (1+monthly_rate)**(duration_in_months - 12*year)
        total_annual_contribution += current_annual_contribution * rate_until_the_end
    total += total_annual_contribution


    return {"Total": total}
