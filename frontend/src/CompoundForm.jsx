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

    const [result, setResult] = useState(null);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const url = "http://127.0.0.1:8000/calculator/calculate"
            const response = await axios.post(url, form);
            console.log('Response:', response.data);
            setResult(response.data);
        } catch (err) {
            console.error('Error:', err);
        }
    };

    return (
        <div style={{ maxWidth: '600px', margin: '0 auto' }}>
            <form onSubmit={handleSubmit}>

                <div style={{ marginBottom: '10px' }}>
                    <input name="initialAmount" type="number" placeholder="Initial Amount" onChange={handleChange} />
                </div>

                <div style={{ marginBottom: '10px' }}>
                    <input name="monthlyContribution" type="number" placeholder="Monthly Contribution" onChange={handleChange} />
                </div>

                <div style={{ marginBottom: '10px' }}>
                    <input name="percetageInterestRate" type="number" placeholder="Interest Rate (%)" onChange={handleChange} />
                    <select name="interestRateType" onChange={handleChange}>
                        <option value="annual">Annual</option>
                        <option value="monthly">Monthly</option>
                    </select>
                </div>

                <div style={{ marginBottom: '10px' }}>
                    <input name="period" type="number" placeholder="Period" onChange={handleChange} />
                    <select name="periodType" onChange={handleChange}>
                        <option value="years">Years</option>
                        <option value="months">Months</option>
                    </select>
                </div>

                <div style={{ marginBottom: '10px' }}>
                    <input name="annualContribution" type="number" placeholder="annualContribution" onChange={handleChange} />
                </div>

                <div style={{ marginBottom: '10px' }}>
                    <input name="percetageAnnualContributionGrowth" type="number" placeholder="Annual Contribution Growth (%)" onChange={handleChange} />
                </div>

                <button type="submit" style={{ width: '100%', padding: '10px' }}>Calculate</button>
            </form>

            {result && (
                <div style={{ marginTop: '30px' }}>
                    <h3>Results</h3>
                    <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                        <thead>
                            <tr>
                                <th style={{ border: '1px solid #ddd', padding: '8px' }}>Event</th>
                                <th style={{ border: '1px solid #ddd', padding: '8px' }}>Value</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style={{ border: '1px solid #ddd', padding: '8px' }}>Total Invested</td>
                                <td style={{ border: '1px solid #ddd', padding: '8px' }}>R${result["Total Invested"].toFixed(2)}</td>
                            </tr>
                            <tr>
                                <td style={{ border: '1px solid #ddd', padding: '8px' }}>Total Interest Earnings</td>
                                <td style={{ border: '1px solid #ddd', padding: '8px' }}>R${result["Total Interest Earnings"].toFixed(2)}</td>
                            </tr>
                            <tr>
                                <td style={{ border: '1px solid #ddd', padding: '8px' }}>
                                    <strong>Total</strong>
                                </td>
                                <td style={{ border: '1px solid #ddd', padding: '8px' }}>
                                    <strong>R${result.Total.toFixed(2)}</strong>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
};

export default CompoundForm;