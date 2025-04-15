import React, { useState } from 'react'
import axios from 'axios';

const CompoundForm = () => {
    const [form, setForm] = useState({
        initialAmount: '',
        monthlyContribution: '',
        percetageInterestRate: '',
        interestRateType: 'Annual',
        period: '',
        periodType: 'Years',
        annualContribution: '0',
        percetageAnnualContributionGrowth: '',
    });


    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const url = "http://127.0.0.1:8000/calculator/calculate"
            const response = await axios.post(url, form);
            console.log('Response:', response.data);
            // show the result on the screen later
        } catch (err) {
            console.error('Error:', err);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input name="initialAmount" type="number" placeholder="Initial Amount" onChange={handleChange} />
            <input name="monthlyContribution" type="number" placeholder="Monthly Contribution" onChange={handleChange} />
            <input name="percetageInterestRate" type="number" placeholder="Interest Rate (%)" onChange={handleChange} />

            <select name="interestRateType" onChange={handleChange}>
                <option value="annual">Annual</option>
                <option value="monthly">Monthly</option>
            </select>

            <input name="period" type="number" placeholder="Period" onChange={handleChange} />
            <select name="periodType" onChange={handleChange}>
                <option value="years">Years</option>
                <option value="months">Months</option>
            </select>
            <input name="annualContribution" type="number" placeholder="annualContribution" onChange={handleChange} />
            <input name="contributionGrowth" type="number" placeholder="Annual Contribution Growth (%)" onChange={handleChange} />

            <button type="submit">Calculate</button>
        </form>
    );
};

export default CompoundForm;