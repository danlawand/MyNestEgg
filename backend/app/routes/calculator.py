from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

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
    initialAmount = float(data.initialAmount)
    monthlyContribution = float(data.monthlyContribution)
    percetageInterestRate = float(data.percetageInterestRate)
    period = int(data.period)
    annualContribution = float(data.annualContribution)
    percetageAnnualContributionGrowth = float(data.percetageAnnualContributionGrowth)
    interestRateType = data.interestRateType
    periodType = data.periodType

    isInterestRateAnnual = interestRateType=="Annual"
    isPeriodInYears = periodType=="Years"
    totalInvested = 0
    interestRate = percetageInterestRate/100
    annualContributionGrowth = percetageAnnualContributionGrowth/100
    
    if not isPeriodInYears:
        periodInYears = period//12
        periodInMonths = period
    else:
        periodInYears = period
        periodInMonths = period*12
    
    if isInterestRateAnnual:
        monthlyRate = (1 + interestRate)**(1/12) - 1
    else:
        monthlyRate = interestRate

    total = initialAmount * (1+monthlyRate)**periodInMonths

    monthlyTotal = 0
    for year in range(periodInYears):
        totalInvested += monthlyContribution*12
        currentMonthlyContribution = monthlyContribution * (1+annualContributionGrowth)**year 
        twelveMonthRate = (1+monthlyRate)**(periodInMonths - 12*year) 
        rateUntilTheEnd = (1+monthlyRate)**(periodInMonths - 12*(year+1))
        monthlyTotal += currentMonthlyContribution * ((twelveMonthRate-rateUntilTheEnd)/monthlyRate)
    total += monthlyTotal

    totalAnnualContribution = 0
    for year in range(1, periodInYears+1):
        totalInvested += annualContribution
        currentAnnualContribution = annualContribution * (1+annualContributionGrowth)**(year-1)
        rateUntilTheEnd = (1+monthlyRate)**(periodInMonths - 12*year)
        totalAnnualContribution += currentAnnualContribution * rateUntilTheEnd
    total += totalAnnualContribution
    totalInterestEarnings =  total-totalInvested

    return {"Total": total, "Total Invested": totalInvested, "Total Interest Earnings": totalInterestEarnings}
