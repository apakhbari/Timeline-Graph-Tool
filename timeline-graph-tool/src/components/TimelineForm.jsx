import React, { useState } from 'react';

const TimelineForm = ({ onSubmit }) => {
  const [startYear, setStartYear] = useState('');
  const [endYear, setEndYear] = useState('');
  // Initialize with three job objects
  const [jobs, setJobs] = useState([
    { name: '', start: '', end: '' },
    { name: '', start: '', end: '' },
    { name: '', start: '', end: '' },
  ]);

  const handleJobChange = (index, field, value) => {
    const updatedJobs = [...jobs];
    updatedJobs[index][field] = value;
    setJobs(updatedJobs);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Pass the collected timeline data to the parent component
    onSubmit({ startYear, endYear, jobs });
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 card bg-base-100 shadow-xl">
      <div className="form-control">
        <label className="label">
          <span className="label-text">Enter starting year of the timeline</span>
        </label>
        <input
          type="number"
          placeholder="e.g., 2015"
          className="input input-bordered"
          value={startYear}
          onChange={(e) => setStartYear(e.target.value)}
          required
        />
      </div>
      <div className="form-control mt-4">
        <label className="label">
          <span className="label-text">Enter ending year of the timeline</span>
        </label>
        <input
          type="number"
          placeholder="e.g., 2024"
          className="input input-bordered"
          value={endYear}
          onChange={(e) => setEndYear(e.target.value)}
          required
        />
      </div>
      <div className="mt-4">
        <h2 className="text-xl font-bold">Jobs</h2>
        {jobs.map((job, index) => (
          <div key={index} className="border p-2 my-2 rounded">
            <div className="form-control">
              <label className="label">
                <span className="label-text">Job {index + 1} Name</span>
              </label>
              <input
                type="text"
                placeholder="Job name"
                className="input input-bordered"
                value={job.name}
                onChange={(e) => handleJobChange(index, 'name', e.target.value)}
                required
              />
            </div>
            <div className="form-control mt-2">
              <label className="label">
                <span className="label-text">Start Date (YYYY-MM)</span>
              </label>
              <input
                type="month"
                className="input input-bordered"
                value={job.start}
                onChange={(e) => handleJobChange(index, 'start', e.target.value)}
                required
              />
            </div>
            <div className="form-control mt-2">
              <label className="label">
                <span className="label-text">End Date (YYYY-MM or 'present')</span>
              </label>
              <input
                type="text"
                placeholder="YYYY-MM or present"
                className="input input-bordered"
                value={job.end}
                onChange={(e) => handleJobChange(index, 'end', e.target.value)}
                required
              />
            </div>
          </div>
        ))}
      </div>
      <button type="submit" className="btn btn-primary mt-4">
        Generate Graph
      </button>
    </form>
  );
};

export default TimelineForm;
