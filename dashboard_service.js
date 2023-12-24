```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

const DashboardService = () => {
    const [sentimentData, setSentimentData] = useState([]);
    const [entityData, setEntityData] = useState([]);
    const [syntaxData, setSyntaxData] = useState([]);
    const [imageData, setImageData] = useState([]);
    const [audioData, setAudioData] = useState([]);

    useEffect(() => {
        fetchAnalysisData();
    }, []);

    const fetchAnalysisData = async () => {
        try {
            const sentimentResponse = await axios.get('/api/analyze/sentiment');
            const entityResponse = await axios.get('/api/analyze/entity');
            const syntaxResponse = await axios.get('/api/analyze/syntax');
            const imageResponse = await axios.get('/api/analyze/image');
            const audioResponse = await axios.get('/api/analyze/audio');

            setSentimentData(sentimentResponse.data);
            setEntityData(entityResponse.data);
            setSyntaxData(syntaxResponse.data);
            setImageData(imageResponse.data);
            setAudioData(audioResponse.data);
        } catch (error) {
            console.error('Error fetching analysis data:', error);
        }
    };

    const formatChartData = (data) => {
        return {
            labels: data.map(item => item.label),
            datasets: [{
                label: '# of Votes',
                data: data.map(item => item.count),
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        };
    };

    return (
        <div>
            <h1>Smart Content Analyzer Dashboard</h1>
            <div>
                <h2>Sentiment Analysis</h2>
                <Bar data={formatChartData(sentimentData)} />
            </div>
            <div>
                <h2>Entity Analysis</h2>
                <Bar data={formatChartData(entityData)} />
            </div>
            <div>
                <h2>Syntax Analysis</h2>
                <Bar data={formatChartData(syntaxData)} />
            </div>
            <div>
                <h2>Image Analysis</h2>
                <Bar data={formatChartData(imageData)} />
            </div>
            <div>
                <h2>Audio Analysis</h2>
                <Bar data={formatChartData(audioData)} />
            </div>
        </div>
    );
};

export default DashboardService;
```
