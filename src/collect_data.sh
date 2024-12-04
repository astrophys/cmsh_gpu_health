#!/bin/bash
 
 
for((i=1; i<10; i++)); do
    echo "${HOSTSTEM}g0${i}"
    for((g=0; g<8; g++)); do
        cmsh -c "device; dumpmonitoringdata -6d now gpu_temperature:gpu${g} -n ${HOSTSTEM}g0${i}" > ${HOSTSTEM}g0${i}_gputemp_gpu${g}.txt
        cmsh -c "device; dumpmonitoringdata -6d now gpu_utilization:gpu${g} -n ${HOSTSTEM}g0${i}" > ${HOSTSTEM}g0${i}_gpuutil_gpu${g}.txt
    done;
done;
 
for((i=10; i<=31; i++)); do
    echo "${HOSTSTEM}g${i}"
    for((g=0; g<8; g++)); do
        cmsh -c "device; dumpmonitoringdata -6d now gpu_temperature:gpu${g} -n ${HOSTSTEM}g${i}" > ${HOSTSTEM}g${i}_gputemp_gpu${g}.txt
        cmsh -c "device; dumpmonitoringdata -6d now gpu_utilization:gpu${g} -n ${HOSTSTEM}g${i}" > ${HOSTSTEM}g${i}_gpuutil_gpu${g}.txt
    done;
done;
