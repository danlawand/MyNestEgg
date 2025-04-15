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


class CalculationRequest(BaseModel):
    initialAmount: float
    monthlyContribution: float
    percetageInterestRate: float
    interestRateType: str
    period: int
    periodType: str
    annualContribution: float
    percetageAnnualContributionGrowth: float

@router.post("/calculate/")
def calulate(
    data: CalculationRequest
):
    return {"message": f"Received: {data}"}

    # initialAmount = data.initialAmount
    # monthlyContribution = data.monthlyContribution
    # percetageInterestRate = data.percetageInterestRate
    # interestRateType = data.interestRateType
    # period = data.period
    # periodType = data.periodType
    # annualContribution = data.annualContribution
    # percetageAnnualContributionGrowth = data.percetageAnnualContributionGrowth

    # init_amount = float(initialAmount)
    # monthly_contribution = float(monthlyContribution)
    # percetage_interest_rate = float(percetageInterestRate)
    # rate_type = interestRateType
    # period = int(period)
    # period_type = periodType
    # annual_contribution = float(annualContribution)
    # percetage_annual_contribution_growth = float(percetageAnnualContributionGrowth)

    # is_interest_rate_annual = rate_type=="Annual"
    # is_period_in_years = period_type=="Years"
    # total_invested = 0
    # interest_rate = percetage_interest_rate/100
    # annual_contribution_growth = percetage_annual_contribution_growth/100
    
    # if not is_period_in_years:
    #     period_in_years = period//12
    #     period_in_months = period
    # else:
    #     period_in_years = period
    #     period_in_months = period*12
    
    # if is_interest_rate_annual:
    #     monthly_rate = (1 + interest_rate)**(1/12) - 1
    # else:
    #     monthly_rate = interest_rate

    # total = init_amount * (1+monthly_rate)**period_in_months

    # monthly_total = 0
    # for year in range(period_in_years):
    #     total_invested += monthly_contribution*12
    #     current_monthly_contribution = monthly_contribution * (1+annual_contribution_growth)**year 
    #     twelve_month_rate = (1+monthly_rate)**(period_in_months - 12*year) 
    #     rate_until_the_end = (1+monthly_rate)**(period_in_months - 12*(year+1))
    #     monthly_total += current_monthly_contribution * ((twelve_month_rate-rate_until_the_end)/monthly_rate)
    # total += monthly_total

    # total_annual_contribution = 0
    # for year in range(1, period_in_years+1):
    #     total_invested += annual_contribution
    #     current_annual_contribution = annual_contribution * (1+annual_contribution_growth)**(year-1)
    #     rate_until_the_end = (1+monthly_rate)**(period_in_months - 12*year)
    #     total_annual_contribution += current_annual_contribution * rate_until_the_end
    # total += total_annual_contribution
    # total_interest_earnings =  total-total_invested

    # return {"Total": total, "Total Invested": total_invested, "Total Interest Earnings": total_interest_earnings}
