Homework 4. Kubernetes
----------------

## Commands
### Kubernetes cluster information
```
kubectl cluster-info
```

### Kubernetes start pod
```
kubectl apply -f kubernetes_manifests/online-inference-pod.yaml
```

### Kubernetes start pod
```
kubectl apply -f kubernetes_manifests/online-inference-pod.yaml
```

### Kubernetes get pod
```
kubectl get pods
```

## Evaluation criteria

| # |  | Description | Score |
| --- | --- | --- | --- |
| 0 | :ballot_box_with_check: | Установите kubectl | 0 |
| 1 | :ballot_box_with_check: | Разверните kubernetes | 5 |
| 2 | :ballot_box_with_check: | Напишите простой pod manifests для вашего приложения, назовите его online-inference-pod.yaml (https://kubernetes.io/docs/concepts/workloads/pods/). Задеплойте приложение в кластер (kubectl apply -f online-inference-pod.yaml), убедитесь, что все поднялось (kubectl get pods) Приложите скриншот, где видно, что все поднялось | 4 |
| 2a | :ballot_box_with_check: | Пропишите requests/limits и напишите зачем это нужно в описание PR. Pакоммитьте файл online-inference-pod-resources.yaml| 2 |
------------
