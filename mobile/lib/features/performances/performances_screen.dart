import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class PerformancesScreen extends StatelessWidget {
  const PerformancesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Performances')),
      body: const Center(child: Text('Tu historial aparecerá aquí.')),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () => context.push('/performances/record'),
        icon: const Icon(Icons.videocam_outlined),
        label: const Text('Grabar'),
      ),
    );
  }
}
