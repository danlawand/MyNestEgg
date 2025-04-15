from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CalculatorSettings(BaseModel):
    init_amount: float
    monthly_contribution: float
    percetage_interest_rate: float
    is_interest_rate_annual: bool
    period: int
    is_period_in_years: bool
    annual_contribution: float | None = None
    percetage_annual_contribution_growth: float | None = None


@router.post("/calculate/")
def calulate(
    settings: CalculatorSettings
):
    total_invested = 0
    interest_rate = settings.percetage_interest_rate/100
    annual_contribution_growth = settings.percetage_annual_contribution_growth/100
    
    if not settings.is_period_in_years:
        period_in_years = settings.period//12
        period_in_months = settings.period
    else:
        period_in_years = settings.period
        period_in_months = settings.period*12
    
    if settings.is_interest_rate_annual:
        monthly_rate = (1 + interest_rate)**(1/12) - 1
    else:
        monthly_rate = interest_rate

    total = settings.init_amount * (1+monthly_rate)**period_in_months

    monthly_total = 0
    for year in range(period_in_years):
        total_invested += settings.monthly_contribution*12
        current_monthly_contribution = settings.monthly_contribution * (1+annual_contribution_growth)**year 
        twelve_month_rate = (1+monthly_rate)**(period_in_months - 12*year) 
        rate_until_the_end = (1+monthly_rate)**(period_in_months - 12*(year+1))
        monthly_total += current_monthly_contribution * ((twelve_month_rate-rate_until_the_end)/monthly_rate)
    total += monthly_total

    total_annual_contribution = 0
    for year in range(1, period_in_years+1):
        total_invested += settings.annual_contribution
        current_annual_contribution = settings.annual_contribution * (1+annual_contribution_growth)**(year-1)
        rate_until_the_end = (1+monthly_rate)**(period_in_months - 12*year)
        total_annual_contribution += current_annual_contribution * rate_until_the_end
    total += total_annual_contribution
    total_interest_earnings =  total-total_invested

    return {"Total": total, "Total Invested": total_invested, "Total Interest Earnings": total_interest_earnings}
