import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const TimelineGraph = ({ data }) => {
  const { startYear, endYear, jobs } = data;
  
  // Create main timeline data: one point per year (placed at y = 0)
  const mainTimelineData = [];
  for (let year = Number(startYear); year <= Number(endYear); year++) {
    mainTimelineData.push({
      date: new Date(year, 0, 1).getTime(),
      label: year.toString(),
      y: 0,
    });
  }

  // For each job, create a line with two points: start and end.
  // Each job gets a unique vertical offset.
  const jobLines = jobs.map((job, index) => {
    const yOffset = (index + 1) * 50; // 50 units apart vertically
    const startTime = new Date(job.start + "-01").getTime();
    const endTime =
      job.end.toLowerCase() === 'present'
        ? new Date(endYear, 11, 31).getTime()
        : new Date(job.end + "-01").getTime();
    return {
      name: job.name,
      data: [
        { date: startTime, y: yOffset },
        { date: endTime, y: yOffset },
      ],
    };
  });

  return (
    <div style={{ width: '100%', height: 400 }}>
      <ResponsiveContainer>
        <LineChart margin={{ top: 20, right: 30, left: 20, bottom: 20 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis
            dataKey="date"
            type="number"
            domain={['dataMin', 'dataMax']}
            tickFormatter={(tick) => new Date(tick).getFullYear()}
          />
          <YAxis hide={true} />
          <Tooltip labelFormatter={(label) => new Date(label).toLocaleDateString()} />
          {/* Main timeline line */}
          <Line
            data={mainTimelineData}
            type="monotone"
            dataKey="y"
            stroke="#8884d8"
            strokeWidth={2}
            dot={{ r: 5, stroke: '#8884d8', strokeWidth: 2 }}
            isAnimationActive={false}
          />
          {/* Render each job line */}
          {jobLines.map((jobLine, idx) => (
            <Line
              key={idx}
              data={jobLine.data}
              type="monotone"
              dataKey="y"
              name={jobLine.name}
              stroke="#82ca9d"
              strokeWidth={4}
              dot={{ r: 5, stroke: '#82ca9d', strokeWidth: 2 }}
              isAnimationActive={false}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default TimelineGraph;
