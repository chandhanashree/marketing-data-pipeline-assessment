SELECT
    AVG(max_temp) AS average_max_temperature,
    AVG(min_temp) AS average_min_temperature,
    AVG(temp_range) AS average_temperature_range
FROM weather_data;