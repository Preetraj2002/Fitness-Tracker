import streamlit as st


def calculate_sleep_index(
    total_duration, deep_sleep_duration, light_sleep_duration, rem_sleep_duration
):
    # Calculate Sleep Efficiency
    sleep_efficiency = (
        (deep_sleep_duration + light_sleep_duration + rem_sleep_duration)
        / total_duration
    ) * 100

    # Calculate Sleep Index
    if sleep_efficiency < 85:
        sleep_index = "Poor"
    elif 85 <= sleep_efficiency < 90:
        sleep_index = "Fair"
    elif 90 <= sleep_efficiency < 95:
        sleep_index = "Good"
    else:
        sleep_index = "Excellent"

    return sleep_index


def sleep_quality_tracker( user_id, conn):
    st.title("Sleep Quality Tracker")

    # Timestamp input
    timestamp = st.date_input("Date")

    # Total duration input
    total_duration = st.number_input("Total Sleep Duration (minutes)")

    # Deep sleep duration input
    deep_sleep_duration = st.number_input("Deep Sleep Duration (minutes)")

    # Light sleep duration input
    light_sleep_duration = st.number_input("Light Sleep Duration (minutes)")

    # REM sleep duration input
    rem_sleep_duration = st.number_input("REM Sleep Duration (minutes)")

    # Submit button
    if st.button("Submit"):
        # Calculate sleep index
        sleep_index = calculate_sleep_index(
            total_duration,
            deep_sleep_duration,
            light_sleep_duration,
            rem_sleep_duration,
        )

        # Display sleep index
        st.success(f"Sleep Index: {sleep_index}")


def main():
    sleep_data_input()


if __name__ == "__main__":
    main()
