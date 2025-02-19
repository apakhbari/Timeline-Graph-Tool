import React, { useState } from 'react';
import TimelineForm from './components/TimelineForm';
import TimelineGraph from './components/TimelineGraph';

function App() {
  const [timelineData, setTimelineData] = useState(null);

  const handleFormSubmit = (data) => {
    setTimelineData(data);
  };

  return (
    <div className="min-h-screen p-4 bg-base-200">
      <header className="mb-4">
        <h1 className="text-3xl font-bold text-center">Time Series Graph Tool</h1>
      </header>
      <div className="flex flex-col md:flex-row gap-4">
        <div className="w-full md:w-1/3">
          <TimelineForm onSubmit={handleFormSubmit} />
        </div>
        <div className="w-full md:w-2/3">
          {timelineData ? (
            <TimelineGraph data={timelineData} />
          ) : (
            <p className="text-center">Fill out the form to generate the timeline graph.</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
