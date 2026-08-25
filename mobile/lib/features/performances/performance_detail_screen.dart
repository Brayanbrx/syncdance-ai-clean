import 'package:flutter/material.dart';

class PerformanceDetailScreen extends StatelessWidget {
  const PerformanceDetailScreen({required this.performanceId, super.key});

  final String performanceId;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Performance #$performanceId')),
      body: const Center(
        child: Text('El resultado del análisis aparecerá aquí.'),
      ),
    );
  }
}
